from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Integer, MetaData, String, func
from cbot.db                    import CRUD
from decimal                    import Decimal, getcontext
from sqlalchemy.orm.attributes  import flag_modified

Base = declarative_base()

class Order(Base, CRUD):
    getcontext().prec = 9

    __tablename__ = 'orders'

    id                      = Column(Integer, primary_key=True)
    purchase_rate           = Column('purchase_rate', Integer)
    btc_quantity            = Column('btc_quantity', Integer)
    sold_at_rate            = Column('sold_at_rate', Integer)
    minium_profitable_rate  = Column('minium_profitable_rate', Integer)
    external_id             = Column('external_id', String)
    status                  = Column('status', String)
    settled                 = Column('settled', String)

    def __repr__(self):
        return '''
        <Order(purchase_rate='%s',
                btc_quantity='%s',
                sold_at_rate='%s',
                minium_profitable_rate='%s',
                external_id='%s',
                settled='%s',
                status='%s')>
        ''' % (self.purchase_rate, self.btc_quantity,
               self.sold_at_rate, self.minium_profitable_rate,
               self.external_id, self.settled, self.status) 

    @classmethod
    def profitable(self, current_price):
        return self.query(self).filter(
                #  [wipn] make sure this won't break because of orders that don't have a mpr yet
                self.minium_profitable_rate <= Decimal(current_price)).all()

    @classmethod
    def pending(self):
        return self.query(self).filter(self.status == 'pending').all()

    @classmethod
    def all(self):
        return self.query(self).all()

    @classmethod
    def create_purchase(self, record):
        order = Order(
                external_id=record.get('id'),
                purchase_value=Decimal(record.get('funds')),
                purchase_rate=record.get('executed_value'),
                btc_quantity=Decimal(record.get('filled_size')),
                settled=record.get('settled'),
                status=record.get('status'),
            )
        session.add(order)
        session.commit()
        return order

    @classmethod
    def execute_purchase(self, record):
        self.purchase_rate=Decimal(record.get('executed_value'))
        self.btc_quantity=Decimal(record.get('filled_size'))
        self.status=record.get('status')
        self._set_mpr()
        self.save()
        return self

    def _set_mpr(self):
        self.minimum_profitable_rate = self._calculate_mpr()

    def _calculate_mpr(self):
        self.purchase_rate * 0.02 + self.purchase_rate
