import os, sys
ROOT_DIR =os.path.realpath(os.path.join(os.path.abspath('__file__'), '..')) 
sys.path.append(os.path.join(ROOT_DIR))
from model.DBModel import DBModel
from sqlalchemy import func

class DropTable:
        
    def __str__(self):
        return ('Drop Data Object')
        
    def getBalance(self, sqldb):
        total_balance = sqldb.session.query(DBModel).with_entities(func.sum(DBModel.income).label('balance')).first().balance
        return '%.2f'%total_balance  
    
    def dropAllData(self, sqldb):
        sqldb.drop_all()
        sqldb.create_all()
        x= sqldb.session.commit()
        return 0 
    
    