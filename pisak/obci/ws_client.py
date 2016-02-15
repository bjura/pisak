import json

from ws4py.client.threadedclient import WebSocketClient


SERVER_HOST = '127.0.0.1'
SERVER_PORT = '28394'


class Client(WebSocketClient):

    SERVER_ADDRESS = 'ws://{}/ws'.format(
        ":".join([SERVER_HOST, SERVER_PORT]))

    def __init__(self, on_new_msg):
        super().__init__(self.SERVER_ADDRESS)
        self._on_new_msg = on_new_msg
        self.connect()

    def received_message(self, msg):
        self._on_new_msg(msg)

    def send_message(self, msg_type, msg_data=None):
        content = {'type': msg_type}
        if msg_data is not None:
            content.update({'data': msg_data})
        self.send(json.dumps(content))
