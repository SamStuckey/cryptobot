from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://samuelstuckey:pass@localhost:5432/cryptobot')
Session = sessionmaker(bind=engine)
session = Session()

class CRUD():
    session = session

    def save(self):
         if self.id == None:
             session.add(self)
         else:
             self.update(self)
         return session.commit()

    def update(self, params={}):
    #  'id': 'cc65dcd7-9aef-4f08-a6c7-28c5cd5ba373',
    #  'product_id': 'BTC-USD',
    #  'side': 'buy',
    #  'stp': 'dc',
    #  'funds': '9.95024875',
    #  'specified_funds': '10',
    #  'type': 'market',
    #  'post_only': False,
    #  'created_at': '2020-07-18T16:45:03.722006Z',
    #  'fill_fees': '0',
    #  'filled_size': '0',
    #  'executed_value': '0',
    #  'status': 'pending',
    #  'settled': False
        external_id = params.get('id')


    def destroy(self):
        session.delete(self)
        return session.commit()

    def query(self):
        return session.query(self)

    def default_query(self):
        return self.session.query(*self.structure)
