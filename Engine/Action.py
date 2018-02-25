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
    def __init__(self,attack,source, target, wrange, adv=False,disadv=False):       
        self.attack=attack
        self.to_hit_stat=self.attack.whateverstat#as incorporated in item as pulled from database
        self.source=source
        self.target=target
        self.wrange=wrange
        if "Multiattack"in self.attack: #have databases contain the number of attacks in each multiattack
            number_attacks=self.attack.numberattacks
            self.totaldamage=0
            for i in range(number_attacks):
                self.damage=dice(database_type[i],database_number[i])#more placeholders
                self.totaldamage+=self.damage
        self.totaldamage=dice(database_type,database_number)#more placeholders
        
    def execute(self):
        self.to_hit_bonus =self.source.stats[self.to_hit_stat]
        self.ac = self.target.ac
        self.hit=hit(self.to_hit_bonus,self.ac,adv,disadv) and (self.wrange>=distance(self.source,self.target))
        if self.hit:
            target.apply_damage(self.totaldamage)
            
            
class Cast(Action):
    def __init__(self,spell,source,target,crange,adv=False,disadv=False):
        self.spell=spell
        self.source=source
        self.target=target
        self.crange=crange
        
    def execute(self):
        
        