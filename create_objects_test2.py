from database import db, db_models
#db.drop_all()
#db.create_all()

db_models.PDB.query[0].ligand="ligand1"

up_entry1 = db_models.Uniprot(acc="P00519_2")
db.session.add(up_entry1)

up_entry2 = db_models.Uniprot(acc="P00519_3")
db.session.add(up_entry2)
                                                    #Relationship points to the uniprot object this way
pdb_entry_1 = db_models.PDB(pdb_id="PDB2", in_bindingdb_validation_set=False, uniprot=up_entry1)
db.session.add(pdb_entry_1)

pdb_entry_2 = db_models.PDB(pdb_id="PDB3", in_bindingdb_validation_set=True, uniprot=up_entry2)
db.session.add(pdb_entry_2)

# db.session.add(up_entry2)
# db.session.add(pdb_entry_2)

db.session.commit()

print 'UniProt table: '
print db_models.Uniprot.query.all()
print 'PDB table: '
print db_models.PDB.query.all()