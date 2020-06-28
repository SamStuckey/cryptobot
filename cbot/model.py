from sqlalchemy import Column, Integer, MetaData# , Table
from sqlalchemy.ext.declarative import declarative_base
from cbot.db    import CRUD
from datetime   import date

Base = declarative_base()

#  meta = MetaData()
#  Table(
#     'orders', meta,
#      Column('id', Integer, primary_key=True),
#      Column('buy_price', Numeric),
#      Column('sell_price', Numeric),
#      Column('bought_at', Numeric),
#      Column('sold_at', Numeric),
#      Column('usd_val', Numeric),
#      Column('btc_val', Numeric)
#  )

#  CREATE TABLE orders (
#          id INT GENERATED ALWAYS AS IDENTITY,
#          buy_price INT,
#          sell_price INT,
#          bought_at INT,
#          sold_at INT,
#          buy_usd_val INT,
#          buy_btc_val INT,
#          sell_usd_val INT,
#          sell_btc_val INT
#          )
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

    def __init__(self):
        pass
