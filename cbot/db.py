from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://samuelstuckey:pass@localhost:5432/cryptobot')
Session = sessionmaker(bind=engine)
session = Session()

class CRUD():
    def save(self):
         if self.id == None:
             session.add(self)
         return session.commit()

    def destroy(self):
        session.delete(self)
        return session.commit()
