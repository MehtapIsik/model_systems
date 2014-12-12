from database import db

# acc = ONE   pdb_id = MANY

class Uniprot(db.Model):
    # __tablename__ = 'uniprot'
    id = db.Column(db.Integer, primary_key = True)
    # uniprot accession number
    acc = db.Column(db.String(64), unique = True)
    pdbs = db.relationship("PDB", backref='uniprot', lazy='dynamic')

    # def __init__(self, acc):
    #     self.acc = acc
    #     # self.PDBs = PDB

    def __repr__(self):
        return "<UniProt %r>" % self.acc

class PDB(db.Model):
    # __tablename__ = 'pdb'
    id = db.Column(db.Integer, primary_key = True)
    pdb_id = db.Column(db.String(64), unique = True)
    in_bindingdb_validation_set = db.Column(db.Boolean)
    ligand = db.Column(db.String(64))
    uniprot_id = db.Column(db.Integer, db.ForeignKey('uniprot.id'))
    # uniprot_acc = db.Column(db.String(64), db.ForeignKey('uniprot.acc'))


    # def __init__(self, pdb_id, present_in_BindingDB_validation_set):
    #     self.pdb_id = pdb_id
    #     self.present_in_BindingDB_validation_set = present_in_BindingDB_validation_set

    def __repr__(self):
         return "<PDB %r>" % self.pdb_id



