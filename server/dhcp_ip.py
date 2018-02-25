
#Use ngrok.exe http 8000 to access server

from twisted.internet import reactor
from twisted.web.resource import Resource

from twisted.web.server import Site
import time
class BusyPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        time.sleep(5)
        return "Finally done, at %s" % (time.asctime(),)

if __name__ == "__main__":
    factory = Site(BusyPage())
    reactor.listenTCP(8000, factory)
    reactor.run()

