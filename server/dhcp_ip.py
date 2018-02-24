#http://jinglei.me/how-to-configure-static-ip-dhcp-python-script-windows/

import sys  
import wmi

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
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)

    if len(colNicConfigs) < 1:
        print("Can not get network configuration")
        exit()

    objNicConfig = colNicConfigs[0]

    val = objNicConfig.EnableDHCP()
    print(val)
    val = objNicConfig.SetDNSServerSearchOrder()
    print(val)  

    print('ip: ', ', '.join(objNicConfig.IPAddress))
    factory = Site(BusyPage())
    reactor.listenTCP(8000, factory)
    reactor.run()

