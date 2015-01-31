# Step 11
###`analyse_chembl_bioactivity_records.py`

Counts the elements in the DataFrames of each target protein(Uniprot ACC) coming from step 10
Starting from the output of Step10 (DataFrame pkl files) and Uniprot ACC list (output of step1, writen as argument variable), this script extracts number of bioactivity records and available drugs for each target protein.


###INPUT
`model_systems/output/step1/uni_acc_str_of_validation_set.txt` - string of Uniprot ACCs(full list coming from BindingDB Validation Set). This one gives error since some protein targets are not found in ChEMBL database. I eliminated those that don't exist in ChEMBL and formed a new list of Uniprot ACCs.
So, use this input instead:

`model_systems/output/step10/uni_acc_str_of_validation_set_missing_acc.txt` - string of Uniprot ACCs (some ACCs present in Validation Set are missing here.)
 
See `/model_systems/other_files/manual_interventions_to_model_systems_database_building.odt` for more detail.

`model_systems/output/step10` - DataFrame pkl files for each target


###OUTPUT
`model_systems/output/step11/` 

Output is plk files for dataFrames: 

* Number of Bioactivity Records vs Uniprot ACC 

* Number of Bioactivity records with unique ligands(ingredient compounds) vs Uniprot ACC 

* Number of Ki/IC50/Kd type bioactivity records vs Uniprot ACC

* number of approved drugs vs Uniprot ACC 
