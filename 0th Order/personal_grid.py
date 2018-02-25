import numpy as np
import matplotlib.pyplot as plt

class Grid:
    def __init__(self,x,y,N):    
        self.x=x
        self.y=y
        self.N=N  #N must be odd

    def create_local_grid(self):
        return grid_x,grid_y=np.meshgrid(np.arange(floor(self.N/2),np.arangefloor(self.N/2))
        
