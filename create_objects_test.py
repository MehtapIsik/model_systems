from database import db, db_models
db.drop_all()
db.create_all()

up_entry1 = db_models.Uniprot(acc="P00519")
db.session.add(up_entry1)
# up_entry2 = UniProt("acc 2" pdb_entry_2)

                                                    #Relationship points to the uniprot object this way
pdb_entry_1 = db_models.PDB(pdb_id="PDB1", in_bindingdb_validation_set=False, uniprot=up_entry1)

                                                    #This doest work, use the line above first
# pdb_entry_1 = db_models.PDB(pdb_id="PDB1", in_bindingdb_validation_set=False, uniprot_id=up_entry1.id)

                            #This format of relationship works for acc since acc is defined for each object
# pdb_entry_1 = db_models.PDB(pdb_id="PDB1", in_bindingdb_validation_set=True, uniprot_acc=up_entry1.acc)
# pdb_entry_2 = db_models.PDB(pdb_id="PDB2", in_bindingdb_validation_set=False, uniprot_acc=up_entry1.acc)

db.session.add(pdb_entry_1)

# db.session.add(up_entry2)
# db.session.add(pdb_entry_2)

db.session.commit()

print 'UniProt table: '
print db_models.Uniprot.query.all()
print 'PDB table: '
print db_models.PDB.query.all()