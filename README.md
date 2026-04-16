# Biological Databases & Ontology Workflows

This repository contains a collection of bioinformatics workflows for retrieving and processing biological data from NCBI databases using multiple programming approaches.

---

##  Project Overview

The aim of this project is to demonstrate reproducible data retrieval and transformation workflows using:

- **R**
- **Python**
- **Bash**

These workflows cover both **single accession retrieval** and **batch data processing** from the Sequence Read Archive (SRA).

---

## Repository Structure (Branches)

Each branch represents a specific workflow:

###  1. `r-single-accession`
- Retrieve a single GenBank accession using R
- Outputs:
  - FASTA
  - GenBank (.gb)
  - Metadata (.csv)
  - Full metadata (.json)

---

### 2. `r-multiple-sra`
- Download multiple SRA accessions using R
- Automates batch retrieval of FASTQ files

---

###  3. `python-multiple-sra`
- Python-based workflow for downloading multiple SRA datasets

---

###  4. `bash-multiple-sra`
- Command-line (Bash) workflow using SRA Toolkit

---

##  Technologies Used

- R (`rentrez`, `xml2`, `jsonlite`, `tidyverse`)
- Python
- Bash (SRA Toolkit)
- Git & GitHub for version control

---

##  Key Concepts Demonstrated

- Programmatic access to NCBI databases  
- Handling multiple bioinformatics file formats  
- Batch processing using loops  
- Reproducible workflows using RMarkdown  
- Structured project organization using Git branches  

---

##  Getting Started

Clone the repository:

```bash
git clone https://github.com/N-mogoi/biological_databases_ontology.git
cd biological_databases_ontology


Switch to a branch of interest:

```bash
git checkout r-single-accession


Author

Nick Mogoi
Bioinformatics | R | Python | Genomics

Connect
GitHub: https://github.com/N-mogoi
LinkedIn: www.linkedin.com/in/nick-mogoi-2023b2173
