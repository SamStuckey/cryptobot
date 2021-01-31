from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Integer, MetaData, String, func, Float
from cbot.db                    import CRUD
from sqlalchemy.orm.attributes  import flag_modified

Base = declarative_base()

class Order(Base, CRUD):
    __tablename__ = 'orders'

    # cql reset: 
#      CREATE TABLE orders (
    #      id int PRIMARY KEY NOT NULL,
    #      purchase_rate FLOAT,
    #      btc_quantity FLOAT,
    #      minium_profitable_rate FLOAT,
    #      sold_at_rate FLOAT,
    #      usd_value_at_purchase FLOAT,
    #      usd_value_at_sale FLOAT,
    #      external_id VARCHAR,
    #      status VARCHAR,
    #      settled VARCHAR
    #  );
#
    id                      = Column(Integer, primary_key=True)
    purchase_rate           = Column('purchase_rate', Float)
    btc_quantity            = Column('btc_quantity', Float)
    sold_at_rate            = Column('sold_at_rate', Float)
    minium_profitable_rate  = Column('minium_profitable_rate', Float)
    usd_value_at_purchase   = Column('usd_value_at_purchase', Float)
    usd_value_at_sale       = Column('usd_value_at_sale', Float)
    external_id             = Column('external_id', String)
    status                  = Column('status', String)
    settled                 = Column('settled', String)

    def __repr__(self):
        return '''
        <Order(purchase_rate='%s',
                btc_quantity='%s',
                sold_at_rate='%s',
                minium_profitable_rate='%s',
                usd_value_at_purchase='%s',
                usd_value_at_sale='%s',
                external_id='%s',
                settled='%s',
                status='%s')>
        ''' % (self.purchase_rate, self.btc_quantity,
               self.sold_at_rate, self.minium_profitable_rate,
               self.usd_value_at_purchase, self.usd_value_at_sale,
               self.external_id, self.settled, self.status) 

    @classmethod
    def profitable(self, current_price):
        return self.query(self).filter(
                #  [wipn] make sure this won't break because of orders that don't have a mpr yet
                self.minium_profitable_rate <= float(current_price)).all()

    @classmethod
    def pending(self):
        return self.query(self).filter(self.status == 'pending').all()

    @classmethod
    def all(self):
        return self.query(self).all()

    @classmethod
    def create_purchase(self, record, current_price):
        pass
        #  order = Order(
        #          external_id=record.get('id'),
        #          purchase_rate=float(current_price),
        #          usd_value_at_purchase=float(record.get('funds')),
        #          btc_quantity=float(record.get('funds')),
        #          sold_at_rate=float(record.get('funds')),
        #          minium_profitable_rate=float(record.get('funds')),
        #          usd_value_at_purchase=float(record.get('funds')),
        #          settled=record.get('funds')),
        #          status=record.get('funds')),
        #          product_id=record.get('product_id')
        #      )
        #  session.add(order)
        #  session.commit()
        #  return order

    @classmethod
    def execute_purchase(self, record,):
        self.usd_value_at_purchase=float(record.get('executed_value'))
        self.btc_quantity=float(record.get('filled_size'))
        self.status=record.get('status')
        self._set_mpr()
        self.save()
        return self

    def _set_mpr(self):
        self.minimum_profitable_rate = self._calculate_mpr()

    def _calculate_mpr(self):
        self.purchase_rate * 0.02 + self.purchase_rate
