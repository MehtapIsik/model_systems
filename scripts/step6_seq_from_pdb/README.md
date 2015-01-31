# Step 6
###`extract_seq_from_pdb_with_PdbIO.py`

Extracts amino acid sequence information from PDB file(SEQRES lines in PDB file) and prints it out.

### `extract_seq_from_pdb_coordinates.py`
Parses a given pdb file, to extract structural information. Prints out sequence based on resolved coordinates in crystal structure.

Amino acid residues present in SEQRES but that doesn't have coordinate information are listed in REMARK 465 of PDB file

###INPUT
`model_systems/output/step4/` - `uniprotACC_PDBID.pdb.gz` symlink files

Copy Step4 output files to `model_system/input/step6/` to use this script.
