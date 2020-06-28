from cbot.app import Cbot
from decouple import config

interval  = config('INTERVAL')
time_in_force  = config('TIME_IN_FORCE')

cbot = Cbot(interval, time_in_force)
cbot()
