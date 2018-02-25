# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 00:53:57 2018

@author: abenn
"""
#import numpy as np 




def makeattackdict(file):
    #import numpy as np 
    #import re
    attackaskey=dict()
    numberidaskey=dict()
   # for k, v in thedict.items():
       # print(k, v)
    f=open(file, "r")
    #f.close()
    
    
    line=f.readline()
    #line=f.readline()
    #print(line[0])
       
    
    ######################START ARRAY LOOP
    newcounter=0
    attacks=[]
    while(newcounter<106):
        #print(line[0])
        line=f.readline()
        firstcommalocations=[] #first2
        
        
        for i in range(0,len(line)):
            if (line[i]==','):
                firstcommalocations.append(i)
                if(len(firstcommalocations)>3):
                    break
        
        thisattack=[]
        #print(firstcommalocations[0])
        #print(newcounter)
        
        for i in range(firstcommalocations[0]+1,firstcommalocations[1]):
            
            thisattack.append(line[i])
        stringattack="".join(thisattack)
        attacks.append(stringattack)
        newcounter+=1
        #print(stringattack)
         ######################END ARRAY LOOP
    #print(attacks)
    #print(attacks[3])
        
        
       
        
        ######################START DICT LOOP
    counter=0
    while(counter<106):
        
        currentattack=attacks[counter]
        currentnumberid=str(counter+1)
        #print(currentattack)
        attackaskey[currentattack]=counter+1
        numberidaskey[currentnumberid]=currentattack
        
        
        counter+=1
    #print(attackaskey["Shatter"]) 
    #print(numberidaskey["106"])
    #print(attackaskey)   
        
        
        
        
        
        
        
        
        ######################END ARRAY LOOP
        


makeattackdict("spreadsheets\Attacks.csv")
