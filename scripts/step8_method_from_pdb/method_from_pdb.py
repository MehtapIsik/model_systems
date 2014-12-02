# extracts method information from PDB file by looking at EXPDTA label
#
# usage:  python method_from_pdb.py pdbfile.pdb.gz

from sys import argv
import os
import gzip

#unpacking
script, pdb_filename = argv

#define input and output path
input_path = "../../input/step8"
output_path = "../../output/step8"

pdb_file = gzip.open(os.path.join(input_path, pdb_filename), 'r')
#pdb_file_content = pdb_file.read()

#print lines starting with "EXPDTA "
for line in pdb_file:
    if line.startswith('EXPDTA'):
        print line


