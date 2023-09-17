from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class Datastore:
    def __init__(self):
        host=os.getenv('DB_HOST')
        database=os.getenv('DB_NAME')
        username=os.getenv('DB_USERNAME')
        password=os.getenv('DB_PASSWORD')

        self._engine = create_engine(f'postgresql://{username}{(":" + password) if password else password }@{host}/{database}')
    
    def __del__(self):
        self._engine.dispose()
    
    def get_first(self, model, conds={}):
        session = scoped_session(sessionmaker(bind=self._engine))

        query = session.query(model)
        for attr, value in conds.items():
            query = query.filter(getattr(model, attr) == value)

        res = query.first()

        return res

    def get_with_limit(self, model, limit=-1, conds={}):
        session = scoped_session(sessionmaker(bind=self._engine))

        query = session.query(model)
        for attr, value in conds.items():
            query = query.filter(getattr(model, attr) == value)

        if limit == -1:
            return query.all()

        return query.limit(limit).all()
    
    def create(self, model, conds={}):
        m = model

        prev = self.get_first(m.__class__, conds)
        if prev:
            return prev

        session = scoped_session(sessionmaker(bind=self._engine, expire_on_commit=False))

        session.add(m)
        session.commit()

        return m
    
    def update(self, model, conds={}, fields_to_update={}):
        m = model
        session = scoped_session(sessionmaker(bind=self._engine, expire_on_commit=False))

        query = session.query(m)
        for attr, value in conds.iteritems():
            query = query.filter(getattr(m, attr) == value)

        query.update(fields_to_update)
        session.expunge_all()
        session.commit()
        
        return m
