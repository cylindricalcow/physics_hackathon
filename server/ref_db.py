#Test for calling databases with Twisted

#https://twistedmatrix.com/documents/15.3.0/core/howto/rdbms.html
#https://gist.github.com/PolBaladas/07bfcdefb5c1c57cdeb5
#https://www.pythonlearn.com/html-008/cfbook015.html
# Create connection...
import sqlite3 
conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',('Africa by Toto', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',('All Star by Smashmouth',15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur :
   print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()


# Using the "dbmodule" from the previous example, create a ConnectionPool
from twisted.enterprise import adbapi
dbpool = adbapi.ConnectionPool("sqlite3", 'conn',)

# equivalent of cursor.execute(statement), return cursor.fetchall():
def getPlays(title):
    print(title," get played was called")
    return dbpool.runQuery("SELECT plays FROM Tracks WHERE name = ?", title)

def printResult(l):
    if l:
        print(l[0][0], " is the song")
    else:
        print("No such song")

getPlays("Africa by Toto").addCallback(printResult)
