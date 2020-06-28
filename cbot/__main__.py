#  from cbot.app import Cbot
#  from decouple import config
#
#  interval  = config('INTERVAL')
#  time_in_force  = config('TIME_IN_FORCE')
#
#  cbot = Cbot(db, interval, time_in_force)
#  cbot()
#
""" below this line is test, above is actual app """
from cbot.model import Order

order = Order()
order.save()
print(order)
