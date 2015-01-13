# Exploring model protein ligand binding systems

Database being built starting from BindingDB Validation Set for searching binding model systems.

----
## Protocol
* PDB ID's from [BindingDB Validation Set](http://www.bindingdb.org/validation_sets/index.jsp) are extracted
* Each PDB ID is mapped to Uniprot Accession Number (ACC) 
* Uniprot xml file is downloaded for each Uniprot ACC
* All PDB ID's associated to each Uniprot entry are extracted from xml files
* For each PDB ID, its PDB file is found in Hal cluster and their symlinks are created
* Data about *E.coli* expression, sequence, structure determination method and present non-biopolymer chemical(HET) component is extracted from PDB files.
* SMILES and InChI for each HET is extracted using [Ligand Expo](http://ligand-expo.rcsb.org/)
  

----
## Manifest
* `database/` - directory of [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.0/) database model
* `scripts/` - directory of scripts that generate the database (see `scripts/README.md` for documentation of scripts)
* `input/` - directory of input data for scripts
* `output/` - directory where script outputs are stored
* `create_objects_test.py` - Python script to test creating objects in the database.

