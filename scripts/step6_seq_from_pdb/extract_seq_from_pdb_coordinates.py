# parses a given pdb file, to extract structural information
#
#  run this from model_systems directory
# usage:  python script/step6_seq_from_pdb/extract_seq_from_pdb_coordinates.py pdbfile.pdb.gz

import os
from sys import argv
import gzip
import Bio.PDB
from Bio.PDB.Polypeptide import PPBuilder


#unpacking
script, filename = argv
pdb_filename = filename

#define input and output path
input_path = "input/step6"
output_path = "output/step6"


pdb_file = gzip.open(os.path.join(input_path, filename))
pdb_parser = Bio.PDB.PDBParser(pdb_file)

## to get structural data
pdb_id = pdb_filename[7:11]
structure = pdb_parser.get_structure(pdb_id, pdb_file)

print structure


# Extract sequence from coordinate information
# Amino acid residues present in SEQRES but that doesn't have coordinate information
# are listed in REMARK 465
ppb = PPBuilder()        # PPBuilder uses C--N distance to find polypeptides.
for pp in ppb.build_peptides(structure):
    sequence = pp.get_sequence()
    print "This is the polypeptide sequence of %s" %pdb_id
    print sequence
    print "length of sequence: ", len(sequence)

# OR extract sequence from SEQRES - ?

# when I aligned the sequence output of 1A27 here and the fasta sequence, I see 4 residues missing
# these 4 residues are reported as REMARK 465 MISSING RESIDUES (THE FOLLOWING RESIDUES WERE NOT LOCATED
# IN THE EXPERIMENT)
# does this mean unresolved or missing in protein construct?




