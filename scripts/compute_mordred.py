"""
### Computing mordred chemical descriptors from sdf fies
"""



from rdkit import Chem
from mordred import Calculator, descriptors
import pandas as pd
import os
import sys

def calculate_mordred_descriptors(input_sdf_folder, output_csv):
    """
    Calculate Mordred descriptors for all molecules in an SDF file and save to CSV.
    """
    results = []
    calc = Calculator(descriptors, ignore_3D=True)

    if os.path.isdir(input_sdf_folder):  # If it's a directory, process all files in it
        for file_name in os.listdir(input_sdf_folder):
            if file_name.endswith('.sdf'):
                sdf_path = os.path.join(input_sdf_folder, file_name)
                print(f"Processing file: {sdf_path}")
                molecule_supplier = Chem.SDMolSupplier(sdf_path)

                valid_mol_count = 0
                for mol in molecule_supplier:
                    if mol:
                        valid_mol_count += 1
                        try:
                            calculated_descriptors = calc(mol)
                            descriptor_data = {'FileName': file_name}
                            descriptor_data.update(calculated_descriptors.asdict())
                            results.append(descriptor_data)
                        except Exception as e:
                            print(f"  Skipping molecule in {file_name} due to error: {e}")

                print(f"  Valid molecules processed: {valid_mol_count}")
    else:  # If it's a single SDF file
        sdf_path = input_sdf_folder
        print(f"Processing file: {sdf_path}")
        molecule_supplier = Chem.SDMolSupplier(sdf_path)

        valid_mol_count = 0
        for mol in molecule_supplier:
            if mol:
                valid_mol_count += 1
                try:
                    calculated_descriptors = calc(mol)
                    descriptor_data = {'FileName': os.path.basename(sdf_path)}
                    descriptor_data.update(calculated_descriptors.asdict())
                    results.append(descriptor_data)
                except Exception as e:
                    print(f"  Skipping molecule in {sdf_path} due to error: {e}")

        print(f"  Valid molecules processed: {valid_mol_count}")

    if results:
        df = pd.DataFrame(results)
        df.to_csv(output_csv, index=False)
        print(f"✅ Descriptors saved to: {output_csv}")
    else:
        print("⚠️ No valid molecules found. CSV not written.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compute_mordred.py <input_sdf_folder_or_file> <output_csv_path>")
    else:
        input_file_or_folder = sys.argv[1]
        output_file = sys.argv[2]
        calculate_mordred_descriptors(input_file_or_folder, output_file)
