## snakemake_cheminfo_tools

## Overview
This is a sample Snakemake project for computing **Mordred** chemical descriptors from SDF files. The project leverages Snakemake to automate the workflow of descriptor calculation and output CSV generation. 

## Project Structure

```bash
snakemake_cheminfo_tools/
├── Snakefile                 # Main Snakemake workflow file
├── environment.yaml          # Conda environment file for dependencies
├── scripts/                  # Python scripts used in the pipeline
│   └── compute_mordred.py    # Script to compute Mordred descriptors
├── data/                     # Input data folder
├── results/                  # Output folder
```

## Prerequisites
- **Conda**: This project uses Conda to manage dependencies. Ensure you have Conda installed on your system. 

- **Snakemake**: The workflow depends on Snakemake. To install Snakemake in your Conda environment, running the environ.yml file will ensure it is installed.


## Steps to run:

1. Run the following command to set up the environment-

`conda env create -f environment.yml` <br>
`conda activate snakemake_cheminfo_env` <br>

2. Run the snakemake pipeline-

`snakemake --cores 1`


