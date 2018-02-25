from zope.interface import implementer
from twisted.web.resource import IResource
from twisted.cred.portal import IRealm

@implementer(IRealm)
class PublicHTMLRealm(object):
    #implements(IRealm)
    def __init__(self, root):
        self.root = root
    
    def requestAvatar(self, avatarId, mind, *interfaces):
        if IResource in interfaces:
            return (IResource, self.root, lambda: None)
        raise NotImplementedError()