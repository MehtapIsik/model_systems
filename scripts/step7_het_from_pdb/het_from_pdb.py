# extracts heterogenuous specie information from PDB file: small molecules, ligands, metals etc
#
# usage:  python het_from_pdb.py pdbfile.pdb.gz

from sys import argv
import os
import gzip

#unpacking
script, pdb_filename = argv

#define input and output path
input_path = "../../input/step7"
output_path = "../../output/step7"

pdb_file = gzip.open(os.path.join(input_path, pdb_filename), 'r')
#pdb_file_content = pdb_file.read()

#print lines starting with "HET "
for line in pdb_file:
    if line.startswith('HET '):
        print line

pdb_file.seek(0)

#print lines starting with "HETNAM"
print "HETNAM: "
for line in pdb_file:
    if line.startswith('HETNAM'):
        print line

