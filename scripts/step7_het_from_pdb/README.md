# Step 7
###`het_from_pdb.py`

Extracts non-biopolymer chemical component (heterogen) information from PDB file:
small molecules, ligands, metals etc that are present in PDB structure.

###INPUT
`model_systems/output/step4/` - `uniprotACC_PDBID.pdb.gz` symlink files

Copy Step4 output files to `model_system/input/step7/` to use this script.

###OUTPUT
`model_systems/output/step7/` - `component_list_str_of_PDBID.txt` files contain string of HET 3 letter codes.
