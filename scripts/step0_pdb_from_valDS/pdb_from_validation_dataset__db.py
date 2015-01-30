# run this from model_systems directory as:
#       python scripts/step0_pdb_from_valDS/pdb_from_validation_dataset__db.py
# __author__ = 'mehtap'
#
# This script will be modified in the future to write outputs to the Flask SQLAlchemy database.
# At the moment it doesnt work.
#

import urllib, urllib2
import re
from bs4 import BeautifulSoup
import os
from database import db, db_models

# BindingDB validation data set page
url = 'http://www.bindingdb.org/validation_sets/index.jsp'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
validation_set_page = response.read()

#Defining path to put output files
#path = "/home/mehtap/MEHTAP/model_systems/output/step0"
path = "output/step0"

# Validation data set written to an html file

file = open(os.path.join(path, 'validation_set_page_source.html'), "w")
file.write(validation_set_page)
file.close()


soup = BeautifulSoup(validation_set_page, "html.parser")
# print(soup.prettify())

file = open(os.path.join(path, 'validation_set_page_source_soup.html'), "w")
file.write(soup.prettify().encode("utf8"))
file.close()

# xpath: /html/body/table/tbody/tr[174]/td[2]
# soup.html.body.table.tr.contents

# finds the tags with PDB ID by searching for "structureId"
soup.find_all(href = re.compile("structureId"))

# Prints out the PDB IDs
print "PDB IDs: "
for element in soup.find_all(href = re.compile("structureId")):
    print element.string

# Putting PDB IDs in a list. List elements look like u'1ZFK'
# pdb_list = []
# for element in soup.find_all(href = re.compile("structureId")):
#    pdb_list.append(element.string)
# print pdb_list

# Putting PDB IDs in a list.
# Each PDB ID converted to string before being added to the lisr
pdb_list = []
for element in soup.find_all(href = re.compile("structureId")):
    pdb_list.append(str(element.string))
print "This is pdb_list: ", pdb_list
print "Number of entries in PDB list: ", len(pdb_list)

# To convert PDB list to a space separated string
pdb_list_str = ' '.join(pdb_list)
print "String of PDB IDs: ", pdb_list_str
# print pdb_list_str

#Number of PDBs in string
print "Number of PDB IDs in string: ", (len(pdb_list_str)+1)/5

#Writing PDB list as a string to a file
file = open(os.path.join(path, 'pdb_list_from_bindingDB_validationDB.txt'), "w")
file.write(pdb_list_str)
file.close()

