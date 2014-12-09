# extracts non-biopolymer chemical component (heterogen) information from PDB file:
# small molecules, ligands, metals etc
# pdb documentation: http://www.wwpdb.org/documentation/format33/sect4.html
#
# usage:  python het_from_pdb.py pdbfile.pdb.gz

from sys import argv
import os
import gzip


# Eliminates repeating entries from list. Returns a list with unique elements in the same order
def uniqify_list(a_list):
   # order preserving
   unique_list = []
   for e in a_list:
       if e not in unique_list:
           unique_list.append(e)
   return unique_list


#unpacking
script, pdb_filename = argv

#define input and output path
input_path = "../../input/step7"
output_path = "../../output/step7"

pdb_file = gzip.open(os.path.join(input_path, pdb_filename), 'r')
# pdb_file_content = pdb_file.read()

# print lines starting with "HET "
for line in pdb_file:
    if line.startswith('HET '):
        print line

pdb_file.seek(0)

# print lines starting with "HETNAM"
print "HETNAM: "
for line in pdb_file:
    if line.startswith('HETNAM'):
        print line

pdb_file.seek(0)

# chemical component list
chem_comp_list = []

# write chemical components found in pdb file to a file
for line in pdb_file:
    if line.startswith('HET '):
        chem_comp_list.append(line[7:10].strip())

# Eliminate repeating chemical components
uni_chem_comp_list = uniqify_list(chem_comp_list)

# convert component list to a str
uni_chem_comp_str = ' '.join(uni_chem_comp_list)

# Writing chemical component list as a string to a file
pdb_id = pdb_filename[7:11]
file = open(os.path.join(output_path, "component_list_str_of_" + pdb_id +".txt"), "w")
file.write(uni_chem_comp_str)
file.close()
