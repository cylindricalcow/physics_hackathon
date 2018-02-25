import pandas as pd
import glob
import sys
import os

path="D://physics_hackathon//" 
db_path=path+"Databases//"
string = "Spells"
df=pd.read_csv(path+"CSV//Databases - "+string+".csv")
df.to_sql(string, db_path+string+".db") #Figure out how to make connection string
