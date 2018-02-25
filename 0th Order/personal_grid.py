import numpy as np
import matplotlib.pyplot as plt

class Grid:
    def __init__(self,x,y,N):    
        self.x=x
        self.y=y
        self.N=N

    def create_local_grid(self):
        grid_x,grid_y
