import numpy as np
import matplotlib.pyplot as plt
import math

#These are test classes for the server that will act like the UI. The goal is to get this
#class to work with the engine and server. The grid class 

class Grid:
    #A class for what a person would see on their screen
    def __init__(self,N):    
        self.N=N  #N is gridsize aka vision radius

    def create_local_grid(self):
        return np.meshgrid(np.arange(-1*math.floor(self.N/2),math.floor(self.N/2)),np.arange(-1*math.floor(self.N/2),math.floor(self.N/2)))

    def arrow_endpoint(self, target_x, target_y):
         #Want to make arrow for characters outside of vision. Don't sure if this is a
         #good feature, but it could be useful. Want the arrow to be small on the border
         print(target_x, target_y)
         m,b=np.polyfit([0,target_x],[0,target_y],1)
         line=np.poly1d(m,b)
         x_vals=np.arange(-1*math.floor(self.N),math.floor(self.N))
         y_vals=[m * i + b for i in x_vals]
         print(y_vals)
         return x_vals[-6],y_vals[-6],x_vals[-5],y_vals[-5]
         #for i in range(len(x_vals)):
             #if np.sqrt(y_vals[i]**2 +x_vals[i]**2) >self.N/2:
             #    return x_vals[i-1],y_vals[i-1],x_vals[i],y_vals[i]
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
        distance_challenged=[]
        for i in range(len(x_friends)):
            if (x_friends[i] or y_friends[i])>self.N/2:
                print(self.arrow_endpoint(x_friends[i],y_friends[i]))
                distance_challenged.append(self.arrow_endpoint(x_friends[i],y_friends[i]))
        ax=plt.axes()        
        ax.scatter(x_friends,y_friends, color='blue')
        ax.scatter(monster_coords[0],monster_coords[1], color='red')
        ax.scatter([0],[0], color='green')
        scaler=0.8
        for pair in distance_challenged:
            ax.arrow(scaler*pair[0],scaler*pair[1],scaler*pair[2],scaler*pair[3],head_width=0.2, head_length=0.5, fc='k', ec='k') 
        ax.set_xlim(-1*math.floor(self.N),math.floor(self.N)+2)
        ax.set_ylim(-1*math.floor(self.N),math.floor(self.N)+2)                                 
        ax.grid(True)
        plt.savefig('test_arrow.png')
        plt.show()
    
         
test=Grid(10)
test.plot_map({'Alice':[11,7],'Bob':[2,4], 'Rob':[-3,-2], 'Bobert':[1,5]},[2,2])
