# For a given list of Uniprot Accesion Numbers(Acc) this script extracts ligand information
# form ChEMBL.
#
#  run this from model_systems directory
# input file (string of ACCs) must be located in ~/model_systems/input/step10
# input file comes from step1
#
# usage:    python scripts/step10_chembl_id/get_ligand_info_from_chembl.py input_file
#           python scripts/step10_chembl_id/get_ligand_info_from_chembl.py uni_acc_str_of_validation_set.txt
#           OR for testing
#           python scripts/step10_chembl_id/get_ligand_info_from_chembl.py uni_acc_str_2.txt


from bioservices import *
from sys import argv
import os
from pandas import Series, DataFrame
import pandas as pd
import ipdb

s = ChEMBL(verbose=False)


#define input and output path
input_path = "input/step10"
output_path = "output/step10"

#unpacking and importing input acc string
script, filename = argv
ACCs_file = open(os.path.join(input_path, filename))
ACCs_str= ACCs_file.read()
ACCs_list = ACCs_str.split()  #convert string to a list
print ACCs_list


for acc in ACCs_list:
    #extract protein target information from ChEMBL
    target_info = s.get_target_by_uniprotId(acc)
    #print target_info

    # ipdb.set_trace()

    target_chembl_id = target_info['chemblId']
    #print target_chembl_id

    #ChEMBL bioactivity records queried by target protein's ChEMBL ID
    bioactivities=s.get_target_bioactivities(str(target_chembl_id))
    #print bioactivities

    #Convert bioactivities in json format to pandas DataFrame
    df=DataFrame(list(bioactivities))
    print "For acc %s there are %d bioactivity data." %(acc, len(df.index))

    #Writing dataframe into to a pickle file
    df.to_pickle(os.path.join(output_path, "chembl_bioactivities_of_" + acc +".pkl"))




    #you may want to add a checking step to check if there is any bioactivity data
    #with other units than nM

    #Bioactivity that has Ki, IC50, Kd, Kd1, Kd2 type measurements in nM units
    df2=df[((df.bioactivity_type=="Ki")|(df.bioactivity_type=="IC50")|(df.bioactivity_type=="Kd")|(df.bioactivity_type=="Kd1")|(df.bioactivity_type=="Kd2"))&(df.units=='nM')]
    print "For acc %s there are %d Ki/IC50/Kd type bioactivity data." %(acc, len(df2.index))

    #Summarized table for bioactivity that has Ki, IC50, Kd, Kd1, Kd2 type measurements in nM units
    df2_summary=df2[['ingredient_cmpd_chemblid','bioactivity_type','operator','value','units']]

    #Writing df2_summary into to a pickle file
    df2_summary.to_pickle(os.path.join(output_path, "chembl_bioact_ki_ic50_kd_summary_of_" + acc +".pkl"))




    #Approved drugs for this target
    drugs=s.get_approved_drugs(str(target_chembl_id), frmt='json')
    df_drugs=DataFrame(drugs['approvedDrugs'])
    print "For acc %s there are %d approved drugs." %(acc, len(df_drugs))

    #Writing approved drugs for each target into to a pickle file
    df_drugs.to_pickle(os.path.join(output_path, "chembl_approved_drugs_of_" + acc +".pkl"))




# #Writing bioact_number_list as a string to a file
# print bioact_number_list
# # bioact_number_list_str = ' '.join(str(bioact_number_list))
# bioact_number_list_str = str(bioact_number_list)
# file = open(os.path.join(output_path, 'number_of_bioact.txt'), "w")
# file.write(bioact_number_list_str)
# file.close()






