import pandas as pd
import sqlite3 as lite

path = "C:/Users/Grace Sun/physics_hackathon/CSV" 
db_path = path+'/Databases'
string = "Attacks"
conn = lite.connect(db_path)
df = pd.read_csv(path+"/Databases - "+string+".csv")
df.to_sql(string, conn) #Figure out how to make connection string
