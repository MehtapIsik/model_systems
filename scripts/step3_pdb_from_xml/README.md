# Step 3
###`extract_all_pdb_ids_from_xml.py`

Extracts all PDB IDs related to each xml file(named as uniprotACC.xml). Returns separate files for each ACC  consisting of of  strings of all PDB IDs.

###INPUT
`model_systems/output/step1/uni_acc_str_of_validation_set.txt` - string of unique Uniprot ACCs

###OUTPUT
* `model_systems/output/step3/` - `pdb_list_str_of_uniprotACC.txt` files
* `model_systems/input/step4/` - `pdb_list_str_of_uniprotACC.txt` files
