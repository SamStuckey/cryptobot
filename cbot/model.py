from sqlalchemy import Column, Integer, MetaData, String, func
from sqlalchemy.ext.declarative import declarative_base
#  from sqlalchemy.ext.hybrid import hybrid_property
from cbot.db    import CRUD
from decimal         import Decimal

Base = declarative_base()

# id INT GENERATED ALWAYS AS IDENTITY,
# buy_price INT,
# sell_price INT,
# bought_at INT,
# sold_at INT,
# buy_usd_val INT,
# buy_btc_val INT,
# sell_usd_val INT,
# sell_btc_val INT
class Order(Base, CRUD):
    __tablename__ = 'orders'

    id           = Column(Integer, primary_key=True)
    buy_price    = Column('buy_price', Integer)
    sell_price   = Column('sell_price', Integer)
    bought_at    = Column('bought_at', Integer)
    sold_at      = Column('sold_at', Integer)
    buy_usd_val  = Column('buy_usd_val', Integer)
    buy_btc_val  = Column('buy_btc_val', Integer)
    sell_usd_val = Column('sell_usd_val', Integer)
    sell_btc_val = Column('sell_btc_val', Integer)
    external_id  = Column('external_id', String)
    status       = Column('status', String)

    def __repr__(self):
        return '''
        <Order(buy_price='%s', sell_price='%s', bought_at='%s',
                sold_at='%s', buy_usd_val='%s', buy_btc_val='%s',
                sell_usd_val='%s', sell_btc_val='%s', external_id='%s')>
        ''' % (self.buy_price, self.sell_price, self.bought_at,
               self.sold_at, self.buy_usd_val, self.buy_btc_val,
               self.sell_usd_val, self.sell_btc_val, self.external_id) 

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
        self.query(self).filter(self.status == 'pending')

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
    def build_from_transaction(self, result):
        print('attempting to build with: ', result)
        order = Order(
                external_id=result.get('id'),
                buy_usd_val=result.get('funds'),
                created_at=result.get('created_at'),
                status=result.get('status')
            )
        print('built order: ', order)
        return order

    #  [wipn] start here - im updating pending records that have since executed
    def update_from_cb(record):
        params = 
        self


