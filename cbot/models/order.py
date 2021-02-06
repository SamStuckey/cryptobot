from sqlalchemy                 import Column, Integer, MetaData, String, func, Float
from cbot.models                import Model

class Order(Model):
    __tablename__ = 'orders'

    #  CREATE TABLE orders (
    #      id serial PRIMARY KEY NOT NULL,
    #      purchase_rate FLOAT,
    #      filled_size FLOAT,
    #      minimum_profitable_rate FLOAT,
    #      executed_value FLOAT,
    #      external_id VARCHAR NOT NULL,
    #      product_id VARCHAR,
    #      status VARCHAR NOT NULL,
    #      settled VARCHAR,
    #      side VARCHAR
    #      sold BOOLEAN NOT NULL DEFAULT FALSE
    #  );

    id                      = Column(Integer, primary_key=True)
    purchase_rate           = Column('purchase_rate', Float)
    filled_size             = Column('filled_size', Float)
    minimum_profitable_rate = Column('minimum_profitable_rate', Float)
    executed_value          = Column('executed_value', Float)
    external_id             = Column('external_id', String)
    product_id              = Column('product_id', String)
    status                  = Column('status', String)
    settled                 = Column('settled', String)
    side                    = Column('side', String)
    sold                    = Column('sold', String)

    def __repr__(self):
        return '''
        <Order(purchase_rate='%s',
                filled_size='%s',
                minimum_profitable_rate='%s',
                executed_value='%s',
                external_id='%s',
                product_id='%s',
                status='%s',
                settled='%s',
                side='%s',
                sold='%s')>
        ''' % (self.purchase_rate, self.filled_size,
               self.minimum_profitable_rate, self.executed_value,
               self.external_id, self.product_id, self.status,
               self.settled, self.side, self.sold) 

    @classmethod
    def profitable(self, current_price):
        return self.query(self).filter(
                self.minimum_profitable_rate <= float(current_price),
                sold == False,
                side == 'buy').all()

    @classmethod
    def pending(self):
        return self.query(self).filter(self.status == 'pending').all()

    @classmethod
    def all(self):
        return self.query(self).all()

    @classmethod
    def create(self, record):
        order = Order(
                executed_value=float(record.get('executed_value') or 0),
                external_id=record.get('id'),
                product_id=record.get('product_id'),
                status=record.get('status'),
                settled=record.get('settled'),
                side=record.get('side')
            )
        order.save()
        return order

    def execute(self, record):
        self.executed_value=float(record.get('executed_value'))
        self.filled_size=float(record.get('filled_size'))
        self.status=record.get('status')
        self._set_purchase_rate()
        self._set_mpr()
        self.save()
        return self

    def _set_mpr(self):
        self.minimum_profitable_rate = self._calculate_mpr()

    def _calculate_mpr(self):
        return self.purchase_rate * 0.015 + self.purchase_rate

    def _set_purchase_rate(self):
        self.purchase_rate = self.executed_value * self.filled_size
