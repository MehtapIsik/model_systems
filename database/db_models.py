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
    #ligand column may not be necessary
    ligand = db.Column(db.String(64))
    expressed_in_ecoli = db.Column(db.Boolean)
    expression_system = db.Column(db.String(64))
    #SEQRES sequence
    sequence = db.Column(db.String(1024), unique = True)
    method = db.Column(db.String(64), unique = True)
    uniprot_id = db.Column(db.Integer, db.ForeignKey('uniprot.id'))
    # uniprot_acc = db.Column(db.String(64), db.ForeignKey('uniprot.acc'))
    hets = db.relationship("HET", backref='pdb', lazy='dynamic')

    # def __init__(self, pdb_id, present_in_BindingDB_validation_set):
    #     self.pdb_id = pdb_id
    #     self.present_in_BindingDB_validation_set = present_in_BindingDB_validation_set

    def __repr__(self):
         return "<PDB %r>" % self.pdb_id


class HET(db.Model):
    # __tablename__ = 'het'
    id = db.Column(db.Integer, primary_key = True)
    # component identifier is 3 letter code according to PDB Chemical Components Dictionary
    component_identifier = db.Column(db.String(64), unique = True)
    full_name = db.Column(db.String(64), unique = True)
    smiles = db.Column(db.String(256), unique = True)
    inchi = db.Column(db.String(256), unique = True)
    pdb_table_id = db.Column(db.Integer, db.ForeignKey('PDB.id'))

    def __repr__(self):
        return "<HET %r>" % self.component_identifier
