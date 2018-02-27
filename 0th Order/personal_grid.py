import numpy as np
import matplotlib.pyplot as plt
import math

#These are test classes for the server that will act like the UI. The goal is to get this
#class to work with the engine and server. The grid class 

class Grid:
    #A class for what a person would see on their screen
    def __init__(N):    
        self.N=N  #N is gridsize aka vision radius

    def create_local_grid(self):
        return np.meshgrid(np.arange(-1*floor(self.N/2),floor(self.N/2)),floor(self.N/2),floor(self.N/2)))
        
    def plot_map(self, team_coords, monster_coords):
    #Use server to find teammates positions in the future                                     
    #team_coords is dict of 2 element arrays
    #monster_coords is 2 element array
        grid_x,grid_y=self.create_local_grid()
        x_friends=[]
        y_friends=[]                                 
        for key in team_coords.keys():
            x_friends.append(team_coords[key][0])
            y_friends.append(team_coords[key][1])
        plt.scatter(x_friends,y_friends, color='blue')
        plt.scatter(monster_coords[0],monster_coords[1], color='red')
        plt.scatter([0],[0], color='green')
        plt.xlim(grid_x)
        plt.ylim(grid_y)                                 
        plt.grid(True)
        plt.show()

    def arrow_endpoint(self, target_x, target_y):
         #Want to make arrow for characters outside of vision. Don't sure if this is a
         #good feature, but it could be useful
         pass
         
test=Grid(10)
test.arrow_to_help({'Alice':[11,7],'Bob':[2,4], 'Rob':[3,2], 'Bobert':[0,5]},[2,2])
