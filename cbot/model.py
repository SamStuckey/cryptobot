from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Integer, MetaData, String, func
from cbot.db                    import CRUD
from decimal                    import Decimal, getcontext
from sqlalchemy.orm.attributes  import flag_modified

Base = declarative_base()

class Order(Base, CRUD):
    getcontext().prec = 9

    __tablename__ = 'orders'

    id            = Column(Integer, primary_key=True)
    purchase_rate = Column('purchase_rate', Integer)
    btc_quantity  = Column('btc_quantity', Integer)
    sold_at_rate  = Column('sold_at_rate', Integer)
    external_id   = Column('external_id', String)
    status        = Column('status', String)
    settled       = Column('settled', String)

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
    #  'btc_quantity': '0',
    #  'executed_value': '0',
    #  'status': 'pending',
    #  'settled': False
    def __repr__(self):
        return '''
        <Order(purchase_rate='%s',
                btc_quantity='%s',
                sold_at_rate='%s',
                external_id='%s',
                settled='%s',
                status='%s')>
        ''' % (self.purchase_rate, self.btc_quantity,
               self.sold_at_rate, self.external_id,
               self.settled, self.status) 

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
        return self(order)

    @classmethod
    def pending(self):
        return self.query(self).filter(self.status == 'pending').all()

    @classmethod
    def all(self):
        return self.query(self).all()

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
    def create_purchase(self, record):
        order = Order(
                external_id=record.get('id'),
                purchase_value=Decimal(record.get('funds')),
                purchase_rate=record.get('executed_value')
                btc_quantity=Decimal(record.get('filled_size')),
                settled=record.get('settled'),
                status=record.get('status'),
            )
        session.add(order)
        session.commit()
        return order

    def execute_purchase(self, record):
        self.purchase_rate=Decimal(record.get('executed_value'))
        self.btc_quantity=Decimal(record.get('filled_size'))
        self.status=record.get('status')
        self.save()
        return self

    def cost_to_sell(self, current_price):
        return gross_on_sale(current_price) * 0.005

    def gross_on_sale(self, current_price):
        return self.btc_quantity * current_price

    def net_on_sale(self, current_price):
        return gross_on_sale(current_price) - cost_to_sell(current_price)
