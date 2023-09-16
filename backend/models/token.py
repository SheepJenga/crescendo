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

    def __init__(self, name, supply, minted_date, amount_minted, creator_id):
        self.name = name
        self.supply = supply
        self.minted_date = minted_date
        self.amount_minted = amount_minted
        self.creator_id = creator_id
