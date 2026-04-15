#GenBank Data Retrieval Workflow in R

This project demonstrates a reproducible bioinformatics workflow for retrieving and structuring biological data from NCBI using **R**.

---

## Overview

Using a GenBank accession (**WGL30888.1**), this workflow programmatically retrieves and processes biological data into multiple standard formats used in bioinformatics.

The goal is to demonstrate how **R can be used not only for analysis, but also for data acquisition and transformation** in bioinformatics pipelines.

---

## Features

This script retrieves and generates the following:

- **FASTA file (.fasta)** — raw sequence  
- **GenBank file (.gb)** — annotated biological data  
- **CSV file (.csv)** — structured metadata summary  
- **JSON file (.json)** — full metadata including source qualifiers  

---

## Technologies used

- **R**
- [`rentrez`](https://cran.r-project.org/package=rentrez) — NCBI API access  
- [`xml2`](https://cran.r-project.org/package=xml2) — XML parsing  
- [`jsonlite`](https://cran.r-project.org/package=jsonlite) — JSON conversion  
- [`tidyverse`](https://www.tidyverse.org/) — data handling  

---

## Workflow

Accession ID
↓
NCBI Retrieval (rentrez)
↓
FASTA / GenBank / XML
↓
XML Parsing
↓
CSV (summary) + JSON (full metadata)

---

## Output files

After running the script, the following files are generated:

WGL30888.1.fasta
WGL30888.1.gb
WGL30888.1.csv
WGL30888.1.json


---

## How to run

1. Clone the repository:
```bash
git clone https://github.com/N-mogoi/biological_databases_ontology.git
cd biological_databases_ontology

```

2. Open the RMarkdown file in RStudio:
   30656230_assignment.Rmd

3. Install required packages (if needed):

```
    install.packages(c("rentrez", "xml2", "jsonlite", "tidyverse"))

```

4. Knit the Rmarkdown file


This project demonstrates:

- Programmatic access to biological databases
- Handling multiple bioinformatics file formats
- Parsing structured biological metadata
- Building reproducible workflows

Author:

Nick Mogoi
Bioinformatics | R | Python | Genomics

Connect:
GitHub: https://github.com/N-mogoi
LinkedIn: www.linkedin.com/in/nick-mogoi-2023b2173


Notes:
This project is part of training in Biological Databases and Ontologies, focusing on real-world data retrieval and transformation in bioinformatics.
