import argparse
import os
import shutil
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Hlp = '''
Ce script peut être exécuté avec les options suivantes :

    Pour remplacer le fichier "users.db" s'il existe et créer une nouvelle base de données vide : 
        python setup_db.py --replace
    
    Pour créer une sauvegarde du fichier "users.db" s'il existe : 
        python setup_db.py --backup

    Pour restaurer le fichier "users.db" à partir de la sauvegarde "users.db.bak" : 
        python setup_db.py --restore

    Pour créer une nouvelle base de données vide sans remplacer le fichier "users.db" s'il existe : 
        python setup_db.py
'''

print("Use dbdeploy --guide to display a simple guide. (In french/baguette language at the moment)")


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    login = Column(String)
    desc = Column(String)

def backup_db():
    shutil.copyfile('users.db', 'users.db.bak')
    print('Database backed up to "users.db.bak"')

def restore_db():
    shutil.copyfile('users.db.bak', 'users.db')
    print('Database restored from "users.db.bak"')

parser = argparse.ArgumentParser()
parser.add_argument('--replace', action='store_true', help='replace the existing database')
parser.add_argument('--backup', action='store_true', help='create a backup of the existing database')
parser.add_argument('--restore', action='store_true', help='restore the database from a backup')
parser.add_argument('--guide', action='store_true', help='show a little guide in baguette lang')
args = parser.parse_args()

if args.guide:
    print(Hlp)

if args.replace:
    try:
        os.remove('users.db')
    except OSError:
        pass

if args.backup:
    try:
        backup_db()
    except IOError:
        print('Error: unable to create backup')

if args.restore:
    try:
        restore_db()
    except IOError:
        print('Error: unable to restore from backup')

engine = create_engine('sqlite:///users.db', echo=True)

if not args.backup and not args.restore:
    Base.metadata.create_all(engine)

