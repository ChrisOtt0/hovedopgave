from .socket_handler import SocketHandler

class App:
    def __init__(self):
        self._socket_handler = SocketHandler()

    def run(self):
        """
        For now: starts the socket handler.
        """
        self._socket_handler.handle()