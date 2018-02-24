import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random

class monty_hall:
    '''
    Boxes have the attributes car or goat. Can change number of boxes, switches, number of tests, and cars.
    '''
    def __init__(self, nbox=3,ncar=1,nswitch=1,iter_=100):
        self.nbox=nbox
        self.ncar=ncar
        self.nswitch=nswitch
        self.iter=iter_
    def setup(self):
        curtains=[]
        for i in range(self.ncar):
            curtains.append("car")
        ngoat=self.nbox - self.ncar  
        for i in range(ngoat):
            curtains.append("goat")
        return random.sample(curtains, len(curtains))
    def lets_play_a_game(self):
        curtains_pls=monty_hall.setup(self)
        guess=np.random.choice(self.nbox)
        arr_reveal=np.arange(self.nbox)
        del arr_reveal[guess]
        
        reveal=np.random.choice(arr_reveal,1)
        if curtains[reveal]!='car':
            
        #assume nswitch=1
            arr_final=np.arange(self.nbox)
            del arr_final[reveal]
            del arr_final[guess]
            result=np.random.choice(arr_final,1)
            
        if curtains[result]=='car':
            return 1
        else:
            return 0
    def iter_test(self):
        tally=0
        for i in range(self.iter):
            tally+=lets_play_a_game(self)
        return tally/self.iter
