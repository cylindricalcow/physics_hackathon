import pandas as pd
import sqlite3

path = "C:/Users/Grace Sun/physics_hackathon/" 
db_path = path+'/Databases/'
strings = ["Attacks", "Characters", "Cleric", "Conditions", "Damage Types", "Fighter", "Items", "Monsters", "Rogue", "Save Types", "Spells", "Weapons", "Wizard"]

for string in strings:
	conn = sqlite3.connect(db_path+string+".db")
	df = pd.read_csv(path+"CSV/Databases - "+string+".csv")
	df.to_sql(string, conn, if_exists = 'replace')
	conn.close() 
