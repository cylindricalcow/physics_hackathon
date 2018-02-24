#http://jinglei.me/how-to-configure-static-ip-dhcp-python-script-windows/

import sys  
import wmi

from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        self.transport.write(data)
        


    



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
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    #print("Test!")
    
    reactor.run()
