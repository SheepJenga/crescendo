from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class Relationship(Base):
    __tablename__ = 'relationship'

    id = Column(Integer, primary_key=True, autoincrement=True)
    follower_id = Column(Integer, ForeignKey('account.id'))
    following_id = Column(Integer, ForeignKey('account.id'))

    def __init__(self, follower_id, following_id):
        self.follower_id = follower_id
        self.following_id = following_id
