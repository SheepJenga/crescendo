from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from base import Base

class Token(Base):
    __tablename__ = 'token'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    supply = Column(Integer)
    minted_date = Column(DateTime)
    amount_minted = Column(Integer)
    creator_id = Column(Integer, ForeignKey('creators.id'))
