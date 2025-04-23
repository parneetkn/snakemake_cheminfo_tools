# Snakefile for computing Mordred descriptors into a single CSV

# Configurations
SDF_FOLDER = "data"
RESULTS_FOLDER = "results"
SCRIPT_PATH = "scripts/compute_mordred.py"
OUTPUT_CSV = RESULTS_FOLDER + "/mordred_descriptors.csv"

# Input paths
input_sdf = SDF_FOLDER + "/{sample}"  # Use only one .sdf extension

# Rule to run Mordred descriptor computation
rule all:
    input:
        OUTPUT_CSV

rule compute_mordred:
    input:
        sdf_file=input_sdf  # No extra .sdf here
    output:
        temp_csv=RESULTS_FOLDER + "/{sample}_temp.csv"  # Temporary file for each sample
    shell:
        "python {SCRIPT_PATH} {input.sdf_file} {output.temp_csv}"

rule merge_csv:
    input:
        temp_csvs=expand(RESULTS_FOLDER + "/{sample}_temp.csv", sample=os.listdir(SDF_FOLDER))
    output:
        final_csv=OUTPUT_CSV
    run:
        import pandas as pd
        all_data = []
        for file in input.temp_csvs:
            df = pd.read_csv(file)
            all_data.append(df)
        
        # Concatenate all dataframes into a single one and save
        final_df = pd.concat(all_data, ignore_index=True)
        final_df.to_csv(output.final_csv, index=False)
        print(f"✅ All descriptors saved to: {output.final_csv}")
