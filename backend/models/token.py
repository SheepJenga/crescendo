from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class Token(Base):
    __tablename__ = 'token'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    supply = Column(Integer)
    amount_minted = Column(Integer)
    creator_id = Column(Integer, ForeignKey('creator.id'), unique=True)
    created_at = Column(DateTime, default=func.now())

    def __init__(self, name, supply, creator_id):
        self.name = name
        self.supply = supply
        self.amount_minted = 0
        self.creator_id = creator_id
