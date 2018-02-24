#Twisted Network Programming Essentials,
#Second Edition, by Jessica McKellar and Abe Fettig (O’Reilly). Copyright 2013 Jessica
#McKellar, 978-1-4493-2611-1 

from twisted.internet import reactor
from twisted.web.resource import Resource

from twisted.web.server import Site
import time
class BusyPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        time.sleep(5)
        return "Finally done, at %s" % (time.asctime(),)
factory = Site(BusyPage())
reactor.listenTCP(8000, factory)
reactor.run()
