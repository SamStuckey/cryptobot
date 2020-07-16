from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://samuelstuckey:pass@localhost:5432/cryptobot')
Session = sessionmaker(bind=engine)
session = Session()

class CRUD():
    session = session

    def save(self):
         print('saving')
         if self.id == None:
             session.add(self)
         return session.commit()

    def destroy(self):
        session.delete(self)
        return session.commit()

    def query(self):
        return session.query(self)

    def default_query(self):
        return self.session.query(*self.structure)
