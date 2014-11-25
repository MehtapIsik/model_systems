# parses a given pdb file, two functions
# one returns the expression system
# the other returns True if expression system is E.coli
# usage:  python ecoli_expr.py pdbfile.pdb.gz

import os
from sys import argv
import gzip
import Bio.PDB

def get_header_dict(pdb_filename):
    '''
    for a given pdb file, returns the header in dictionary format
    :param pdb_filename: pdb file
    :return:header of pdb file in dictionary format
    '''
    pdb_file = gzip.open(pdb_filename)
    pdb_parser = Bio.PDB.PDBParser(pdb_file)

    ## to get structural data
    # pdb_id = pdb_filename[7:11]
    # pdb_data = pdb_parser.get_structure(pdb_id, pdb_file)

    ## get header info from pdb file
    # pdb_header = pdb_parser.get_header()

    # file = open(os.path.join(output_path, "pdb_header.txt"), "w")
    # file.write(str(pdb_header))
    # file.close()

    header_dict = Bio.PDB.parse_pdb_header(pdb_file)
    pdb_file.close()
    return header_dict


def get_expr_sys_info(header_dict):
    '''
    Gets expression system info from pdb header dictionary
    :param header_dict: header of pdb file in dictionary format
    :return: the expression system
    '''
    return header_dict['source']['1']['expression_system']

def get_structural__


#unpacking
script, filename = argv
pdb_filename = filename


#define input and output path
input_path = "../../input/step5"
output_path = "../../output/step5"

pdb_header_dict = get_header_dict(os.path.join(input_path, filename))
print "PDB header dictionary: "
print pdb_header_dict

print "Expression system: "
print get_expr_sys_info(pdb_header_dict)

