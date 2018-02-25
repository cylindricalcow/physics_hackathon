import numpy as np
import numpy.random as random
import game_functions as game


class Item:
    def __init__(self, Item_Name, **kwargs):
        self.weight = 0 #This number is queried from database


class Equippable(Item):
    def __init__(self):
        pass

    def equip(character):
        pass

    def unequip(character):
        pass


class Consumable(Item):
    def __init__(self):
        pass

    def consume(character):
        pass

class Weapon(Equippable):
    def __init__(self):
        pass

class Armor(Equippable):
    def __init__(self):
        pass

class Shield(Equippable):
    def __init__(self):
        pass