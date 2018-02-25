import pandas as pd
import sqlite3 as lite

path = "D://physics_hackathon//" 
db_path = path+'//Databases//'
strings = [ "Attacks","Characters", "Conditions", "Damage Types", "Monsters", "Save Types", "Spells", "Weapons"]

for string in strings:
    conn = lite.connect(db_path+string+".db")
    df = pd.read_csv(path+"CSV//Databases - "+string+".csv")
    df.to_sql(string, conn, if_exists = 'replace')
    conn.close()

