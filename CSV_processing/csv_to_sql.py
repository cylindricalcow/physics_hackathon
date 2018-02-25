import pandas as pd
import sqlite3 as lite

<<<<<<< HEAD
path="D://physics_hackathon//" 
db_path=path+"Databases//"
string = "Spells"
df=pd.read_csv(path+"CSV//Databases - "+string+".csv")
df.to_sql(string, db_path+string+".db") #Figure out how to make connection string
=======
path = "C:/Users/Grace Sun/physics_hackathon/CSV" 
db_path = path+'/Databases'
strings = ["Attacks", "Characters", "Conditions", "Damage Types", "Monsters", "Save Types", "Spells", "Weapons"]
conn = lite.connect(db_path)

for string in strings:
	df = pd.read_csv(path+"/Databases - "+string+".csv")
	df.to_sql(string, conn, if_exists = 'replace') 
>>>>>>> 66b10067b31357f02c3e1cd993b25e577faaecbd
