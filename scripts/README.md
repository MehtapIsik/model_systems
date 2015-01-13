## Scripts for exploring model protein ligand binding systems

The scripts must be executed in the given order. 

For each step the input files are read from `model_systems/input/` directory and the output files are written to corresponding subdirectory in `model_systems/output/` directory.

All the scripts must be executed from `model_systems/` path.


## Manifest
----
* `step0_pdb_from_valDS/` - directory that contains the Python script that extracts PDB ID's from [BindingDB Validation Set](http://www.bindingdb.org/validation_sets/index.jsp)
 
* `step1_pdb_to_acc/` - directory that contains the Python script that maps each PDB ID to Uniprot Accession Number (ACC)

* `step2_download_uniprot_xml/` - directory that contains the Python script that downloads Uniprot xml file 

* `step3_pdb_from_xml/` - directory that contains the Python script that extracts all PDB ID's associated to each Uniprot ACC from Uniprot xml files

* `step4_find_pdb_file_and_symlink/` - directory that contains the Python script that finds the PDB file in Hal cluster and creates their symlinks in working directory

* `step5_ecoli_expr/` - directory that contains the Python script that extracts *E.coli* expression information from PDB file

* `step6_seq_from_pdb/`- directory that contains the Python script that extracts sequence information from PDB file's SEQRES section. 

* `step7_het_from_pdb/`- directory that contains the Python script that extracts  non-biopolymer chemical(HET) components that are present in the PDB structure 

* `step8_method_from_pdb/`- directory that contains the Python script that extracts structure determination method of the PDB entry from PDB file

* `step9_get_smiles_for_het/`- directory that contains the Python script that maps 3 letter chemical component identifiers to  SMILES and InChI for each HET using [Ligand Expo](http://ligand-expo.rcsb.org/) query
