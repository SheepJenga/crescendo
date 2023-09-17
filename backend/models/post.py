from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from .base import Base

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    spotify_url = Column(String(500), nullable=False)
    content = Column(String(500), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=func.now())
    user_id = Column(Integer, ForeignKey('account.id'))

    def __init__(self, spotify_url, content, user_id):
        self.spotify_url = spotify_url
        self.content = content
        self.user_id = user_id
    