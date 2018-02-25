import hashlib
from authenticator import *
def hash(username, password, passwordHash):
	return hashlib.md5(password).hexdigest()

realm = Realm()
myPortal = portal.Portal(realm)
checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("user", "pass")
checker = checkers.FilePasswordDB("passwords.txt", hash=hash)