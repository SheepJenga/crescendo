from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from base import Base

class Creator(Base):
    __tablename__ = 'creator'

    id = Column(Integer, primary_key=True)
