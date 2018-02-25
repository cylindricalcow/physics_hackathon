import numpy as np
import numpy.random as random
import game_functions as game
from abc import ABC, abstractmethod
import sqlite3

# run csv_to_sql here
path = "C:/Users/Grace Sun/physics_hackathon/Databases"
# name additional conn based on what databases you want to input; make sure to close conn at the end!
conn1 = sqlite3.connect(path+"Items"+".db") 
c = conn1.cursor()

class Item(ABC):
    def __init__(self, Item_Name, **kwargs):
        #fetchone()[0] for the float
        self.Weight = c.execute('SELECT Weight FROM Items WHERE NAME = ?', [Item_Name]).fetchone()[0] 

#test = Item('Club')
#print(test.Weight)

class Equippable(Item):
    def __init__(self, owner):
        pass

    @abstractmethod
    def equip(character):
        pass

    @abstractmethod
    def unequip(character):
        pass


class Consumable(Item):
    def __init__(self):
        pass

    def consume(character):
        pass

class Weapon(Equippable):
    def __init__(self, **kwargs):
        self.one_handed=False
        self.two_handed=False


class Armor(Equippable):
    def __init__(self):
        pass

class Shield(Equippable):
    def __init__(self):
        pass

conn1.close()