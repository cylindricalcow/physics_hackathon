##http://www.codingwithcody.com/2010/07/03/generate-random-ip-with-python/
import numpy.random as random
def rand_ip():
    not_valid = [10,127,169,172,192]
    first = random.randint(1,256)
    while first in not_valid:
        first = random.randint(1,256)
 
    ip = ".".join([str(first),str(random.randint(1,256)),
    str(random.randint(1,256)),str(random.randint(1,256))])
    return ip

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
    '''
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
    '''
    ip=rand_ip()
    print("IP:",ip)
    factory = Site(BusyPage())
    reactor.listenTCP(ip, factory)
    reactor.run()

