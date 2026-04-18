

"""
Batch SRA downloader v3

Reads accession IDs from stdin and downloads FASTQ files using SRA Toolkit.

Features:
- supports SRR and ERR accessions
- retry mechanism
- multiprocessing
- progress bar
- logging
- metadata retrieval
- validation of accession format
- detection of .rtf files
- logging system
- error handling
- compression of files
- multiprocessing
- progress bar
- live output
- performance tuning
- summary reporting

Author: Nick Mogoi

"""

import sys
import os
import subprocess
import multiprocessing as mp
from tqdm import tqdm
import re
import requests
import time

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

    print(f"Starting download: {acc}", flush=True)

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

            # show live output (IMPORTANT CHANGE)
            result = subprocess.run(cmd)

            if result.returncode == 0:
                print(f"Download complete: {acc}", flush=True)

                compress_files(acc)
                log_success(f"SUCCESS: {acc}")

                # metadata
                meta = fetch_metadata(acc)
                if meta:
                    with open(os.path.join(LOG_DIR, f"{acc}_metadata.txt"), "w") as f:
                        f.write(meta)

                return True

            else:
                raise Exception(f"Non-zero exit status: {result.returncode}")

        except Exception as e:
            print(f"Retry {attempt+1}/{RETRIES} failed for {acc}", flush=True)

            if attempt < RETRIES:
                time.sleep(2)
            else:
                print(f"FAILED: {acc}", flush=True)
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

    total = len(accessions)

    print("="*50)
    print(f"Starting SRA download pipeline")
    print(f"Total accessions: {total}")
    print(f"Threads per download: {THREADS}")
    print("="*50)

    # IMPORTANT: limit pool size (avoid overload)
    pool_size = min(THREADS, total)

    with mp.Pool(processes=pool_size) as pool:
        results = list(tqdm(pool.imap(download_accession, accessions), total=total))

    success = sum(results)
    failed = total - success

    print("\n" + "="*50)
    print("Download summary")
    print("="*50)
    print(f"Total   : {total}")
    print(f"Success : {success}")
    print(f"Failed  : {failed}")
    print("="*50)

    if failed > 0:
        print(f"Check error log: {ERROR_LOG}")

# -----------------------------
if __name__ == "__main__":
    main()

