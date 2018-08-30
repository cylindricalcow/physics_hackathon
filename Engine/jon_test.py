"""
Created on Thur Aug 30 2018

@author: Jonathan Richman
"""

import numpy as np

'''
This is going to be a simple version of the game with limited features.
I just want to make a simple character class that will be general for PC, NPC,
and Monsters.

'''

class Character:
    def __init__(self, current_hp, max_hp, ac, att_bonus_1,att_1,att_bonus_2,att_2,att_bonus_3,att_3,att_bonus_4,att_4):
        self.current_hp=current_hp
        self.max_hp=max_hp
        self.ac=ac
        self.att_bonus_1=att_bonus_1
        self.att_bonus_2=att_bonus_2
        self.att_bonus_3=att_bonus_3
        self.att_bonus_4=att_bonus_4
        self.att_1=att_1
        self.att_2=att_2
        self.att_3=att_3
        self.att_4=att_4

    def roll_attack(self, attack_bonus):
        #add attack bonus to roll
        return np.random.randint(0,high=20)+attack_bonus
    
    def ac_check(self, attack_roll):
        #check to see if attack went through AC
        if attack_roll >= self.ac:
            return True
        else:
            return False

    def check_damage(self, ac_bool, attack, bonus_damage=0):
        #if attack hit, update hp
        #attack is an int for the dice to roll
        #implement bonus damage later
        if ac_bool:
            damage = np.random.randint(0,high=attack) + bonus_damage
            self.current_hp -= damage
    
