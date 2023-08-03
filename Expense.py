import os, sys
ROOT_DIR =os.path.realpath(os.path.join(os.path.abspath('__file__'), '..')) 
sys.path.append(os.path.join(ROOT_DIR))
from model.DBModel import DBModel

class Expense:
    
    def __init__(self, sqldb, amount, code):
        self.amount = amount*code
        self.sqldb = sqldb
        self.model = None
        
    def __str__(self):
        if(self.model):
            return str(self.model.trans_id)
        else:
            return str(-1)
    
    def save(self):
        self.model = DBModel(income=self.amount)
        self.sqldb.session.add(self.model)
        self.sqldb.session.commit()
        