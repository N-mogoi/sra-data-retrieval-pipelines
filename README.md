# BATCH SRA DOWNLOADER (Python)

This is a high-performance Python pipeline for batch downloading sequencing data from the NCBI Sequence Read Archive (SRA).

This tool supports both SRR and ERR accessions and I have designed it for scalability, reproducibility in line with bioinformatics workflows.

---

## Overview

In this project, I have developed a scalable  SRA data retrieval pipeline, evolving from a basic script into a fault-tolerant system. 
The juice here is that it can be applied in solving real bioinformatics problems.

The pipeline integrates:

- SRA Toolkit (`fasterq-dump`)
- multiprocessing for parallel downloads
- retry mechanisms for reliability
- metadata retrieval via ENA API
- structured logging and output management

---

## Features

- batch download from stdin
- supports SRR and ERR accessions
- multiprocessing for parallel downloads
- retry mechanism for failed downloads
- automatic directory structure creation
- logging system (success + error tracking)
- FASTQ compression
- progress tracking using tqdm
- metadata retrieval (ENA API)
- input validation (including RTF detection)
- fault-tolerant execution (continues on failure)

---

## Development evolution

### version 1 — baseline script
- sequential downloads
- minimal structure
- no validation or logging

### version 2 — structured workflow
- input validation (SRR/ERR detection)
- directory structure creation
- logging system (success/error logs)
- error handling (try/except)
- metadata retrieval (ENA API)

### version 3 — production pipeline
- multiprocessing (parallel downloads)
- retry mechanism for failed downloads
- progress tracking (tqdm)
- real-time execution output
- improved performance and scalability
- summary reporting (success vs failure)

---

## Project structure
batch-sra-downloader-python
- src/
	 sra_downloader.py # final production script
	 sra_downloader_v1.py # baseline version
	 sra_downloader_v2.py # intermediate version
-  data/
	 sra_accessions.txt # input file

- fastq/ # output (generated)
- logs/ # logs (generated)
- logerrors/ # error logs (generated)
- temp/ # temporary files│
- requirements.txt
- .gitignore
- README.md

---

## Requirements

### System dependencies

- Python 3.x
- SRA Toolkit installed (`fasterq-dump`)

Check installation:

```bash
which fasterq-dump

```


### Python dependencies

```bash
pip install -r requirements.txt

```

## Usage

Input file format: .txt


## Run the pipeline: you have to be in the project directory where all the files are

```bash
python3 src/sra_downloader.py < data/sra_accessions.txt

```


## Output
FASTQ files
fastq/
─ SRRxxxx_1.fastq.gz
─ SRRxxxx_2.fastq.gz


## Logs
logs/
─ download.log
─ SRRxxxx_metadata.txt


## Metadata retrieval

Metadata is retrieved using the ENA API, including:

- run accession
- organism (scientific name)
- library layout (paired/single-end)


## Performance considerations
- multiprocessing enables parallel downloads
- thread allocation affects performance
- excessive threading may overload system resources
- network speed is a limiting factor


## Error handling
- invalid accessions are logged and skipped
- failed downloads are retried automatically
- persistent failures are written to errors.log
- pipeline continues execution even if some downloads fail


## Design principles

This pipeline was built with:

- reproducibility
- scalability
- fault tolerance
- modularity
- real-world applicability

in mind.

## Future improvements
- CLI argument support (argparse)
- ERR → SRR mapping
- structured metadata export (CSV/JSON)
- Docker containerization
- workflow integration (Snakemake / Nextflow)


## Author

Nick Mogoi

Bioinformatics | HPC | Genomics | R | Python | Bash

## Applications

This pipeline is suitable for:

- pathogen genomics workflows
- RNA-seq data retrieval
- comparative genomics
- high-throughput sequencing projects
