from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String)
    profile_picture = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    creator_id = Column(Integer, ForeignKey('creator.id'), unique=True)
    created_at = Column(DateTime, default=func.now())

    def __init__(self, username, email, first_name, last_name, profile_picture):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture = profile_picture
