# extracts sequence from PDB file
#
#
#  run this from model_systems directory
# usage:  python script/step6_seq_from_pdb/extract_seq_from_pdb_with_PdbIO.py pdbfile.pdb.gz

from sys import argv
import os
import gzip
import Bio.SeqIO



def get_seq_from_pdb_seqres(pdbfile):
    '''
    The sequences are derived from the SEQRES lines in the
    PDB file header, not the atoms of the 3D structure.
    Look at help(SeqIO.PdbIO) for more info.
    :param pdbfile:
    :return: seqres sequence
    '''
    seq_iterator =Bio.SeqIO.PdbIO.PdbSeqresIterator(pdbfile)

    for x in seq_iterator:
        print "chain: ", x.name
        print x.seq



#unpacking
script, pdb_filename = argv

#define input and output path
input_path = "input/step6"
output_path = "output/step6"


pdb_file = gzip.open(os.path.join(input_path, pdb_filename))

print "Sequence from SEQRES:"
get_seq_from_pdb_seqres(pdb_file)

