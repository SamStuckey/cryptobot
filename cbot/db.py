from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

class CRUD():
    session = sessionmaker(bind=create_engine(config('LOCAL_DB_PATH')))()

    def save(self):
        self.session.add(self)
        return self.session.commit()

    def destroy(self):
        self.session.delete(self)
        return self.session.commit()

    def query(self):
        return self.session.query(self)
