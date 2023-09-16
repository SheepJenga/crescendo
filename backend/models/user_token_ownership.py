from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class UserTokenOwnership(Base):
    __tablename__ = 'user_token_ownership'

    user_token_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token_id = Column(Integer, ForeignKey('users.id'))
