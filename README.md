# snakemake_cheminfo_tools

## Overview
This is a sample Snakemake project for computing **Mordred** chemical descriptors from SDF files. The project leverages Snakemake to automate the workflow of descriptor calculation and output CSV generation. 

## Project Structure

The project directory is structured as follows:
snakemake_cheminfo_tools/
├── Snakefile
├── eviron.yaml
├── scripts/
│   └── compute_mordred.py
├── data/
│   └── sdf/  # your input .sdf files go here
├── results/
│   └── mordred/  # output .csv files will be saved here


## Prerequisites
- **Conda**: This project uses Conda to manage dependencies. Ensure you have Conda installed on your system. You can install it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

- **Snakemake**: The workflow depends on Snakemake. To install Snakemake in your Conda environment, use the following command:
  ```bash
  conda install -c conda-forge snakemake


## Steps to run:

1. Run the following command to set up the environment-

conda env create -f environment.yml
conda activate snakemake_cheminfo_env

2. Run the snakemake pipeline-
snakemake --cores 1 


