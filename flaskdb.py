from flask_sqlalchemy import SQLAlchemy
import os, sys
ROOT_DIR =os.path.realpath(os.path.join(os.path.abspath('__file__'), '..')) 
sys.path.append(os.path.join(ROOT_DIR))
from model.DBModel import metadata

db = SQLAlchemy(metadata=metadata)