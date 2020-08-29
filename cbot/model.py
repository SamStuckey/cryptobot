from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Integer, MetaData, String, func
from cbot.db                    import CRUD
from decimal                    import Decimal

Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://samuelstuckey:pass@localhost:5432/cryptobot')
Session = sessionmaker(bind=engine)
session = Session()

class Order(Base, CRUD):
    __tablename__ = 'orders'

    id           = Column(Integer, primary_key=True)
    buy_usd_val  = Column('buy_usd_val', Integer)
    buy_btc_val  = Column('buy_btc_val', Integer)
    sell_usd_val = Column('sell_usd_val', Integer)
    sell_btc_val = Column('sell_btc_val', Integer)
    external_id  = Column('external_id', String)
    status       = Column('status', String)

    def __repr__(self):
        return '''
        <Order(buy_usd_val='%s',
                buy_btc_val='%s',
                sell_usd_val='%s',
                sell_btc_val='%s',
                external_id='%s',
                status='%s')>
        ''' % (self.buy_usd_val, self.buy_btc_val,
               self.sell_usd_val, self.sell_btc_val,
               self.external_id, self.status) 

    ##################
    ## QUERY SCOPES ##
    ##################
    @classmethod
    def profitable(self, current_price):
        return self.query(self).filter(
                self.sell_price <= Decimal(current_price)).all()

    @classmethod
    def lowest_bought_at(self):
        order = self.query(self).order_by(self.buy_price).first()
        print(order)
        return self(order)

    @classmethod
    def pending(self):
        return self.query(self).filter(self.status == 'pending')

    ###############
    ## FACTORIES ##
    ###############
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
    @classmethod
    def create_from_cb(self, record):
        order = Order(
                external_id=record.get('id'),
                buy_usd_val=Decimal(record.get('funds')),
                buy_btc_val=Decimal(record.get('filled_size')),
                sell_usd_val=Decimal(record.get('filled_size')),
                sell_btc_val=Decimal(record.get('filled_size')),
                status=record.get('status')
            )
        #  [wipn] START HERE - record is building, but not saving.  figure out why
        # save to run as is, will not actually transact with coinbase because of
        # stubbed #__call__ in app.py
        session.add(order)
        session.commit()
        return order

    def update_from_cb(record):
        self.update(
                external_id=(record.get('id') or self.external_id),
                buy_usd_val=(Decimal(record.get('executed_value')) or self.buy_usd_val),
                buy_btc_val=(Decimal(record.get('filled_size')) or self.buy_btc_val),
                status=(record.get('status') or self.status)
            )
