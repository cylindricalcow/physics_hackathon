#https://stackoverflow.com/questions/4604580/twisted-server-for-multiple-clients
from test_func import *
from twisted.internet import reactor, protocol

#IP of our Rasberry Pi server
HOST = '192.17.211.73'
PORT = 8080

class MyClient(protocol.Protocol):
    def connectionMade(self):
        print("connected!")
        
class MyClientFactory(protocol.ClientFactory):
    protocol = MyClient

factory = MyClientFactory()
reactor.connectTCP(HOST, PORT, factory)

reactor.run()
