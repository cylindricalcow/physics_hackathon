# encoding utf-8

# importing dependencies
from twisted.web import server, resource
from twisted.internet import reactor, protocol
from application import *
from auth import *
import os
from requesthandler import *
class MyClientFactory(protocol.ClientFactory):
    protocol = MyClient

class Server(object):
	"""Server Side management"""
    def __init__(self, arg):
        super(Server, self).__init__()
        self.port=port
        self.host=host


    def createserver(self):
    #pConnect to the server
        factory = MyClientFactory()            
        reactor.connectTCP(self.host, self.port, factory)
        reactor.run()

    def authenticateclient(self,token):
        #Token will be username,password to be added to     
        root = build_sharing_resource()
        factory = Site(root)
        reactor.listenTCP(self.port, factory)
        print ('server is running on %i' % (self.port,))
        reactor.run()


    def requesthandler(self,dynamic=True, sych= False):
        reactor.listenTCP(self.port, MyHTTPFactory())
        reactor.run()

    def datauploader():
	pass


    def closeserver():
        pass
