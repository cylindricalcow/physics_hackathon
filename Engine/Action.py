# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:31:32 2018

@author: CammieFarruggio
"""

from Character import grappled
from Character import poisoned
from Character import paralyzed
from Character import prone
from Character import petrified
from Character import restrained
from game_functions import *
from game_functions import hit
from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self):
        #self.owner
        super().__init__()
        
    @abstractmethod
    def execute(self):
        pass
    
class WeaponAttack(Action):
    def __init__(self,attack,source,target, wrange,adv=False,disadv=False):       
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
        adv=False
        disadv=False
        #distance=the distance between self and target
        if(target.restrained or target.poisoned or target.paralyzed or (target.prone and distance<=5)):
            adv=True
        if(self.restrained or self.poisoned or (target.prone and distance>5)):
            disadv=True
        self.to_hit_bonus =self.source.stats[self.to_hit_stat]
        self.ac = self.target.ac
        self.hit=hit(self.to_hit_bonus,self.ac,adv,disadv,target) and (self.wrange>=distance(self.source,self.target))
        if self.hit:
            target.apply_damage(self.totaldamage)
            #apply any contitions that the attack causes
            
            
class Cast(Action):
    def __init__(self,spell,source,target,crange,adv=False,disadv=False):
        self.spell=spell
        self.source=source
        self.target=target
        self.crange=crange
        
    def execute(self):
        self.save_stat=a
        
class Dash(Action):
    

class Dodge(Action):
    