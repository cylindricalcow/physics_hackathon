# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:31:32 2018

@author: CammieFarruggio
"""
from game_functions import *
from abc import ABC, abstractmethod
class Action(ABC):
    def __init__(self):
        #self.owner
        super().__init__()
        
    @abstractmethod
    def execute(self):
        pass
    
class WeaponAttack(Action):
    def __init__(self,weapon,source, target, wrange, adv=False,disadv=False):       
        self.weapon=weapon
        self.to_hit_stat=self.weapon.whateverstat#as incorporated in item as pulled from database
        self.source=source
        self.target=target
        self.wrange=wrange
        self.damage=dice(database_type,database_number)#more placeholders
        
    def execute(self,target):
        self.to_hit_bonus =self.source.stats[self.to_hit_stat] and (self.wrange>=distance(self.source,self.target))
        self.ac = self.target.ac
        self.hit=hit(self.to_hit_bonus,self.ac)
        if self.hit:
            target.apply_damage(self.damage)
            
            
class 