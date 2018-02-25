import numpy as np
import matplotlib.pyplot as plt
import math

class Grid:
    def __init__(self,x,y,N):    
        self.x=x
        self.y=y
        self.N=N  #N must be odd

    def create_local_grid(self):
        return np.meshgrid(np.arange(floor(self.N/2),np.arangefloor(self.N/2)))
        
    
    def arrow_to_help(self, team_coords, monster_coords):
    #Use server to find teammates positions in the future                                     
    #team_coords is dict of 2 element arrays
    #monster_coords is 2 element array
        x_friends=[]
        y_friends=[]                                 
        for key in team_coords.keys():
            x_friends.append(team_coords[key][0])
            y_friends.append(team_coords[key][1])
        plt.scatter(x_friends,y_friends, color='blue')
        plt.scatter(monster_coords[0],monster_coords[1], color='red')
       # plt.xlim(np.arange(-math.floor(self.N/2)),math.floor(self.N/2))
       # plt.ylim(np.arange(-math.floor(self.N/2)),math.floor(self.N/2))                                 
        plt.grid(True)
        plt.show()

test=Grid(0,0,10)
test.arrow_to_help({'Bob':[2,4], 'Rob':[3,2], 'Bobert':[0,5]},[2,2])
