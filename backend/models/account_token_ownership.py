from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class AccountTokenOwnership(Base):
    __tablename__ = 'account_token_ownership'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('account.id'))
    token_id = Column(Integer, ForeignKey('account.id'))

    def __init__(self, user_id, token_id):
        self.user_id = user_id
        self.token_id = token_id
