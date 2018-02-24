#https://stackoverflow.com/questions/4604580/twisted-server-for-multiple-clients
from twisted.internet import reactor, protocol

HOST = 'localhost'
PORT = 8000

class MyClient(protocol.Protocol):
    def connectionMade(self):
        print("connected!")

class MyClientFactory(protocol.ClientFactory):
    protocol = MyClient

factory = MyClientFactory()
reactor.connectTCP(HOST, PORT, factory)

reactor.run()
