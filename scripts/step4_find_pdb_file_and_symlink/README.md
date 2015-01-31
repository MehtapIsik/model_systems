# Step 4
###`find_pdb_file_and_symlink.py`

Finds PDB file in MSKCC Cbio Hal cluster and create symlinks of pdb files to working output directory.
Path to PDB files directory: `/cbio/jclab/share/pdb/`

###INPUT
`model_systems/output/step1/uni_acc_str_of_validation_set.txt` - string of unique Uniprot ACCs

###OUTPUT
 `model_systems/output/step4/` - `uniprotACC_PDBID.pdb.gz` symlink files
