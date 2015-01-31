# Step 10
###`smiles_or_inchi_for_het_using_ligand_expo.pysmiles_or_inchi_for_het_using_ligand_expo.py`

For a given list of Uniprot Accesion Numbers(Acc) this script extracts ligand information form ChEMBL.

###INPUT
`model_systems/output/step1/uni_acc_str_of_validation_set.txt` - string of Uniprot ACCs(full list coming from BindingDB Validation Set). This one gives error since some protein targets are not found in ChEMBL database. I eliminated those that don't exist in ChEMBL and formed a new list of Uniprot ACCs.
So, use this input instead:
`model_systems/output/step10/uni_acc_str_of_validation_set_missing_acc.txt` - string of Uniprot ACCs (some ACCs present in Validation Set are missing here.)
 
See `/model_systems/other_files/manual_interventions_to_model_systems_database_building.odt` for more detail.

###OUTPUT
`model_systems/output/step10/` - `chembl_approved_drugs_of_uniprotACC.pkl` files 

`model_systems/output/step10/` -`chembl_bioact_ki_ic50_kd_summary_of_uniprotACC.pkl` files

`model_systems/output/step10/` - `chembl_bioactivities_of_uniprotACC.pkl` files
