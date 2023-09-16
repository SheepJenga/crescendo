from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Token(Base):
    __tablename__ = 'token'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    supply = Column(Integer)
    minted_date = Column(DateTime)
    amount_minted = Column(Integer)
    creator_id = Column(Integer, ForeignKey('creators.id'))
