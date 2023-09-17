from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class Datastore:
    def __init__(self):
        host=os.environ['DB_HOST']
        database=os.environ['DB_NAME']
        username=os.environ['DB_USERNAME']
        password=os.environ['DB_PASSWORD']

        self._engine = create_engine(f'postgresql://{username}{(":" + password) if password else password }@{host}/{database}')
    
    def __del__(self):
        self._engine.dispose()
    
    def get_first(self, model, conds={}):
        session = scoped_session(sessionmaker(bind=self._engine))

        query = session.query(model)
        for attr, value in conds.iteritems():
            query = query.filter(getattr(model, attr) == value)

        return query.first()

    def get_with_limit(self, model, limit=-1, conds={}):
        session = scoped_session(sessionmaker(bind=self._engine))

        query = session.query(model)
        for attr, value in conds.iteritems():
            query = query.filter(getattr(model, attr) == value)

        if limit == -1:
            return query.all()
        
        return query.limit(limit).all()
    
    def create(self, model):
        m = model

        prev = self.get_first(m)
        if not prev:
            return prev.id

        session = scoped_session(sessionmaker(bind=self._engine))

        session.add(m)
        session.commit()

        return m.id
    
    def update(self, model, conds={}, fields_to_update={}):
        m = model
        session = scoped_session(sessionmaker(bind=self._engine))

        query = session.query(m)
        for attr, value in conds.iteritems():
            query = query.filter(getattr(m, attr) == value)

        query.update(fields_to_update)
        session.commit()
        
        return m.id
