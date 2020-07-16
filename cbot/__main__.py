from cbot.websocket import Websocket

ws = Websocket()

try:
    ws.start()
except:
    ws.close()

