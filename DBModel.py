from sqlalchemy import MetaData, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class DBModel(Base):
    
    __tablename__ = 'expense'
    __bind_key__ = 'expense'
    trans_id = Column(Integer, primary_key=True)
    income = Column(Float, nullable=False, default=0)
    
    def __repr__(self):
        return 'Transaction %r' % self.trans_id
    
    def __str__(self):
        return 'Transaction %r' % self.trans_id