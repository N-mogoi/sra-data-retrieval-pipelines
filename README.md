# R workflow: multiple SRA download

This branch contains an R-based workflow for downloading multiple SRA accessions using fasterq-dump.

## contents

- src/R_retrieving_multiple_SRA_files.Rmd → main script
- data/sra_accessions.txt → list of SRA IDs

## requirements

- R
- SRA Toolkit (fasterq-dump installed)

## usage

Run the RMarkdown file to:
- read accession IDs
- download FASTQ files
- compress outputs

Outputs are saved in:
fastq_files/


Author

Nick Mogoi
Bioinformatics | R | Python | Genomics

Connect
GitHub: https://github.com/N-mogoi
LinkedIn: www.linkedin.com/in/nick-mogoi-2023b2173
