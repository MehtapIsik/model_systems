# Starting from the output of Step10 (DataFrame pkl files) and Uniprot ACC list (output of step1,
# writen as argument variable), this script extracts number of bioactivity records and available
# drugs for each target protein.
#
# run this from model_systems directory
#
# input file (string of ACCs) must be located in ~/model_systems/input/step10
# input file comes from step1
#
# usage:    python scripts/step11_chembl_data_analysis/analyse_chembl_bioactivity_records.py input_file
#           python scripts/step11_chembl_data_analysis/analyse_chembl_bioactivity_records.py uni_acc_str_of_validation_set.txt
#           OR for testing
#           python scripts/step11_chembl_data_analysis/analyse_chembl_bioactivity_records.py uni_acc_str_2.txt


from sys import argv
import os
from pandas import Series, DataFrame
import pandas as pd

#define input and output path
input_path_for_acc_list= "input/step10"
input_path = "output/step10" # This is where step10 DataFrame pkl files are.
output_path = "output/step11"

#unpacking and importing input acc string
script, filename = argv
ACCs_file = open(os.path.join(input_path_for_acc_list, filename))
ACCs_str= ACCs_file.read()
ACCs_list = ACCs_str.split()  #convert string to a list
# print ACCs_list


#list for counting number of bioact record in one targets bioactivities
number_of_bioact_list=[]
#list for counting number of unique ingredient compound(ligand) chembl ids in each target's bioactivities
number_of_unique_ingr_cmpds_list=[]

for acc in ACCs_list:
    df=pd.read_pickle(os.path.join(input_path, "chembl_bioactivities_of_" + acc + ".pkl"))

    #counting total bioactivity record number
    number_of_bioact_list.append(len(df))
    # print number_of_bioact_list

    #uniquify DataFrame in terms of ligands(ingredient_cmpd_chemblid)
    df_unique=df.drop_duplicates(subset="ingredient_cmpd_chemblid")
    number_of_unique_ingr_cmpds_list.append(len(df_unique))

df_acc_nbioact = pd.DataFrame({"Uniprot ACC":ACCs_list, "Number of Bioactivity Records": number_of_bioact_list})
print df_acc_nbioact.sort(columns="Number of Bioactivity Records", ascending=False).head()
df_acc_nbioact.to_pickle(os.path.join(output_path, "number_of_bioact_records.pkl"))

df_acc_n_unique_ligands = pd.DataFrame({"Uniprot ACC":ACCs_list, "Number of Bioact. records w/ Unique Ligands(Ingr.cmpd)": number_of_unique_ingr_cmpds_list})
print df_acc_n_unique_ligands.sort(columns="Number of Bioact. records w/ Unique Ligands(Ingr.cmpd)", ascending=False).head()
df_acc_n_unique_ligands.to_pickle(os.path.join(output_path, "number_of_bioact_records_with_unique_ligands.pkl"))



# List for counting the number of records in summarized dataframe
# for bioactivity that has only Ki, IC50, Kd, Kd1, Kd2 type measurements in nM units
# Input is the step10 pkl files, named as chembl_bioact_ki_ic50_kd_summary_of_acc.pkl

number_of_ki_ic50_kd_bioact_list=[]

for acc in ACCs_list:
    df2=pd.read_pickle(os.path.join(input_path, "chembl_bioact_ki_ic50_kd_summary_of_"+acc+".pkl"))

    #counting only Ki, IC50, Kd, Kd1, Kd2 type measurements bioactivity record number
    number_of_ki_ic50_kd_bioact_list.append(len(df2))
    # print number_of_ki_ic50_kd_bioact_list

df_acc_n_ki_ic50_kd_bioact = pd.DataFrame({"Uniprot ACC":ACCs_list, "Number of Ki/IC50/Kd Bioactivity Records": number_of_ki_ic50_kd_bioact_list})
print df_acc_n_ki_ic50_kd_bioact.sort(columns="Number of Ki/IC50/Kd Bioactivity Records", ascending=False).head()
df_acc_n_ki_ic50_kd_bioact.to_pickle(os.path.join(output_path, "number_of_ki_ic50_kd_bioact_records.pkl"))



# Counting the number of available drugs for each Uniprot ACC
# Input is the step10 pkl files, named as chembl_approved_drugs_of_acc.pkl

number_of_drugs_list=[]

for acc in ACCs_list:
    df3=pd.read_pickle(os.path.join(input_path, "chembl_approved_drugs_of_"+acc+".pkl"))

    number_of_drugs_list.append(len(df3))
    # print number_of_drugs_list

df_acc_ndrugs = pd.DataFrame({"Uniprot ACC":ACCs_list, "Number of Approved Drugs": number_of_drugs_list})
print df_acc_ndrugs.sort(columns="Number of Approved Drugs", ascending=False).head()
df_acc_ndrugs.to_pickle(os.path.join(output_path, "number_of_approved_drugs.pkl"))




