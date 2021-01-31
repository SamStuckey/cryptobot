from cbot.websocket import Websocket
ws = Websocket()
try:
    ws.start()
except:
    ws.close()

#  from cbot.app import Cbot
#  Cbot().test_run()
