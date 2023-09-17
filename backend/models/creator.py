from sqlalchemy import Column, Integer
from .base import Base

class Creator(Base):
    __tablename__ = 'creator'

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        return
