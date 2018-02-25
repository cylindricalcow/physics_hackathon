#Twisted Network Programming Essentials,
#Second Edition, by Jessica McKellar and Abe Fettig (O’Reilly). Copyright 2013 Jessica
#McKellar, 978-1-4493-2611-1 

from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET
import time
class BusyPage(Resource):
    isLeaf = True
    def _delayedRender(self, request):
        request.write("Finally done, at %s" % (time.asctime(),))
        request.finish()
    def render_GET(self, request):
        d = deferLater(reactor, 5, lambda: request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET
factory = Site(BusyPage())
reactor.listenTCP(8000, factory)
reactor.run()
