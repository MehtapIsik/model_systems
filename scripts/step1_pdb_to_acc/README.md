# Step 1
###`map_pdb_to_acc.py`

Maps PDB IDs to Uniprot Accession Numbers(ACCs).Writes output of Uniprot Accession Numbers that corresponds to PDB IDs given as input.

###INPUT
`model_systems/input/step1/pdb_list_from_bindingDB_validationDB.txt` or

`model_systems/input/step1/CORRECTED_pdb_list_from_bindingDB_validationDB.txt` 

I manually corrected 5 outdated PDB IDs to correct ones in `CORRECTED_pdb_list_from_bindingDB_validationDB.txt`


These are:
2H7L -> 4TRJ,
2H7I -> 4U07,
2H7M -> 4TZK,
2H7P -> 4TZT,
2H7N -> 4U0K

###OUTPUT
`model_systems/output/step1/uni_acc_str_of_validation_set.txt` - string of unique Uniprot ACCs
