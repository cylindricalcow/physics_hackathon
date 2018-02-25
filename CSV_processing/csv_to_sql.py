import pandas as pd
import sqlite3 as lite

path = "C:/Users/Grace Sun/physics_hackathon/CSV" 
db_path = path+'/Databases'
strings = ["Attacks", "Characters", "Conditions", "Damage Types", "Monsters", "Save Types", "Spells", "Weapons"]
conn = lite.connect(db_path)

for string in strings:
	df = pd.read_csv(path+"/Databases - "+string+".csv")
	df.to_sql(string, conn, if_exists = 'replace') 