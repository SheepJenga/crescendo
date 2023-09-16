from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Creator(Base):
    __tablename__ = 'creator'

    id = Column(Integer, primary_key=True)
