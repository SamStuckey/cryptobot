from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

engine = create_engine(config('LOCAL_DB_PATH'))
Session = sessionmaker(bind=engine)
session = Session()

class CRUD():
    session = session

    def save(self):
        session.add(self)
        return session.commit()

    def update(self, params={}):
        self(params).save
        external_id = params.get('id')

    def destroy(self):
        session.delete(self)
        return session.commit()

    def query(self):
        return session.query(self)

    def default_query(self):
        return self.session.query(*self.structure)
