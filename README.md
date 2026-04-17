#  Bash & PBS Workflow: Batch Download of SRA FASTQ Files

This branch houses  a high-performance, scalable workflow for downloading multiple sequencing datasets from the NCBI Sequence Read Archive (SRA) using **Bash scripting** and **PBS job scheduling on HPC**.

---

## Overview

This workflow automates the download of multiple SRA accessions listed in a text file. It is designed for execution on a High-Performance Computing (HPC) environment using a PBS scheduler.

Key features:

- Batch processing using Bash loops
- HPC job submission using PBS
- Parallelized downloads with `fasterq-dump`
- Automatic compression of FASTQ files
- Error handling and logging
- Reproducible and scalable pipeline design

---

## Project structure

bash-multiple-sra (bash workflow)
│
├── scripts/
│ └── sra_downloads.pbs # PBS job script
│
├── data/
│ └── sra_accessions.txt # List of SRA accessions
│
├── logs/ # Output and error logs (generated)
├── sra_downloads/ # FASTQ output directory (generated)
└── README.md



---

##  Input

A plain text file containing SRA accessions:
SRR5985999
SRR5986126
SRR6027661
SRR5986159


## Output

For each accession:


SRRXXXXXXX_1.fastq.gz
SRRXXXXXXX_2.fastq.gz

Expected:
- 10 accessions → 20 FASTQ files (paired-end)

---

##  Requirements

### HPC Environment
- PBS job scheduler (`qsub`)
- Module system enabled

---

### Load Required Modules

```bash
module purge
module load perl/5.26.1
module load app/sratools/3.0.1

```

### Verify installation

```bash
which fasterq-dump
```
/apps/sratoolkit/bin/fasterq-dump


### How to run

1. Navigate to project directory

2. Submit job to HPC

3. Monitor job

4. Check logs

5. Verify downloaded files with ls -lh



### Best Practices

i. Always test commands interactively before submitting jobs
ii. Uee absolute paths for reliability
iii. Compress FASTQ files immediately to save storage
iv. Log failures for reproducibility
v. Separate input, scripts, and outputs



### Key skills

i. HPC job scheduling (PBS)
ii. Parallel processing of sequencing data
iii. Integration of bioinformatics tools in Bash
iv. File system management in pipelines
v. Debugging real-world HPC issues


##  Author

Nick Mogoi
Bioinformatics | HPC | Genomics | R | Python | Bash


## Repository

Main project:
https://github.com/N-mogoi/biological_databases_ontology









