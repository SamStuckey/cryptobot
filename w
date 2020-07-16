from sqlalchemy import Column, Integer, MetaData, String
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

    structure = {
        'id': id,
        'buy_price': buy_price,
        'sell_price': sell_price,
        'bought_at': bought_at,
        'sold_at': sold_at,
        'buy_usd_val': buy_btc_val,
        'buy_btc_val': buy_btc_val,
        'sell_usd_val': sell_usd_val,
        'sell_btc_val': sell_btc_val,
        'external_id': external_id
    }

    args = structure.keys()

    def __init__(self,
            buy_price=None,
            thing=None):
        #  self.id           = params['id']
        self.buy_price = buy_price
        #  self.sell_price   = params[2]
        #  self.bought_at    = params[3]
        #  self.sold_at      = params[4]
        #  self.buy_usd_val  = params[5]
        #  self.buy_btc_val  = params[6]
        #  self.sell_usd_val = params[7]
        #  self.sell_btc_val = params[8]
        #  self.external_id  = params[9]


    @classmethod
    def profitable(self, current_price):
        if current_price is not None:
            print(current_price)
            orders = self.default_query(self).filter(self.sell_price <= Decimal(current_price)).all()
            print(orders)
        #  collection = []
        #  for order in orders:
        #      collection.append(self(order))
        #  return collection
