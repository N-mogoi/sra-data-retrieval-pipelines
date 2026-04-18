

"""
Batch SRA downloader v1

Reads accession IDs from stdin and downloads FASTQ files using SRA Toolkit.

Features:
- supports SRR and ERR accessions
- retry mechanism
- multiprocessing
- progress bar
- logging
- metadata retrieval

Author: Nick Mogoi
"""

import sys
import os
import subprocess
import multiprocessing as mp
from tqdm import tqdm
import re


# -----------------------------
# configuration
# -----------------------------
THREADS = 4
RETRIES = 2

FASTQ_DIR = "fastq"
LOG_DIR = "logs"
ERROR_DIR = "errors"
TEMP_DIR = "temp"

SUCCESS_LOG = os.path.join(LOG_DIR, "download.log")
ERROR_LOG = os.path.join(ERROR_DIR, "errors.log")

# -----------------------------
# setup directories
# -----------------------------
def setup_directories():
    for d in [FASTQ_DIR, LOG_DIR, ERROR_DIR, TEMP_DIR]:
        os.makedirs(d, exist_ok=True)

# -----------------------------
# validate input
# -----------------------------
def validate_input(lines):
    accessions = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # detect RTF
        if line.startswith("{\\rtf"):
            print("Error: input file is RTF, not plain text")
            sys.exit(1)

        if re.match(r"^(SRR|ERR)\d+$", line):
            accessions.append(line)
        else:
            log_error(f"Invalid accession: {line}")

    return list(set(accessions))

# -----------------------------
# logging
# -----------------------------
def log_success(msg):
    with open(SUCCESS_LOG, "a") as f:
        f.write(msg + "\n")

def log_error(msg):
    with open(ERROR_LOG, "a") as f:
        f.write(msg + "\n")

# -----------------------------
# metadata retrieval (ENA API)
# -----------------------------
def fetch_metadata(acc):
    url = f"https://www.ebi.ac.uk/ena/portal/api/filereport?accession={acc}&result=read_run&fields=run_accession,scientific_name,library_layout"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.text.strip()
    except:
        return None

# -----------------------------
# download function
# -----------------------------
def download_accession(acc):

    for attempt in range(RETRIES + 1):

        try:
            cmd = [
                "fasterq-dump",
                acc,
                "--split-files",
                "--threads", str(THREADS),
                "--temp", TEMP_DIR,
                "-O", FASTQ_DIR
            ]

            result = subprocess.run(cmd, capture_output=True)

            if result.returncode == 0:
                compress_files(acc)
                log_success(f"SUCCESS: {acc}")

                meta = fetch_metadata(acc)
                if meta:
                    with open(os.path.join(LOG_DIR, f"{acc}_metadata.txt"), "w") as f:
                        f.write(meta)

                return True

            else:
                raise Exception(result.stderr.decode())

        except Exception as e:
            if attempt < RETRIES:
                time.sleep(2)
            else:
                log_error(f"FAILED: {acc} | {str(e)}")
                return False

# -----------------------------
# compression
# -----------------------------
def compress_files(acc):
    for suffix in ["_1.fastq", "_2.fastq"]:
        f = os.path.join(FASTQ_DIR, acc + suffix)
        if os.path.exists(f):
            subprocess.run(["gzip", f])

# -----------------------------
# main
# -----------------------------
def main():

    setup_directories()

    lines = sys.stdin.readlines()

    accessions = validate_input(lines)

    if not accessions:
        print("No valid accessions found")
        sys.exit(1)

    print(f"Processing {len(accessions)} accessions...")

    pool = mp.Pool(processes=THREADS)

    results = list(tqdm(pool.imap(download_accession, accessions), total=len(accessions)))

    pool.close()
    pool.join()

    success = sum(results)
    failed = len(results) - success

    print("\nSummary:")
    print(f"Total: {len(accessions)}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")

# -----------------------------
if __name__ == "__main__":
    main()