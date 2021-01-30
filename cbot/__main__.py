from cbot.websocket import Websocket

#  [wipn] keep
ws = Websocket()
try:
    ws.start()
except:
    ws.close()

#  [wipn] for single fire testing
#  from cbot.app import Cbot
#  Cbot()(1)
