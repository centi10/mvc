import os, sys
ROOT_DIR =os.path.realpath(os.path.join(os.path.abspath('__file__'), '..')) 
sys.path.append(os.path.join(ROOT_DIR))
from model.DBModel import DBModel
from sqlalchemy import func

class Balance:
        
    def __str__(self):
        return ('Balance query')
        
    def getBalance(self, sqldb):
        total_balance = sqldb.session.query(DBModel).with_entities(func.sum(DBModel.income).label('balance')).first().balance
        if not total_balance:
            total_balance = 0
        return '%.2f'%total_balance    
        