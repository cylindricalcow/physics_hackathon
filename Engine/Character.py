import game_functions as game
import numpy as np
import numpy.random as random


class Character:
    def __init__(self, raceclass='human fighter',new_player=False, **kwargs):
        self.raceclass = raceclass
        if new_player:
        #in stats/stat_mods, index 0-5 correspond to STR, DEX, CON,INT, WIS, and CHA respectively
            self.stats = self.statline()  # Needs to be user defined. Use Kivy
            self.stat_mods = self.modifiers(self.stats)
            self.ac=10+self.stat_mods[1]#+ac of equipped armor
            self.XP = 0
            self.speed=30#-slow effect from armor #dummy values : will pull from database
            self.level = self.lvl(self.XP)
            self.prof = self.proficiency(self.level)
        # Dummy code, the dice command depends on a character's raceclass
            self.hp = game.dice(8) + self.stat_mods[2]
            self.items=[]#again: starting items? class-dependent?
            self.equipped_items=[]
        # dice roll will be dependent on weapon attack values in database
            self.weapon_damage = self.proficiency(self.level)+self.stat_mods[0]+game.dice(8)
            self.magic_user=False #depeding on class info from database
            if self.magic_user:
                make_spell_slots
                
             def make_spell_slots(self)   
                self.max_cast_level=seeclass #add from database depending on level
                self.cantrips=seeclass#again, add from database depending on class/level
                self.spell_slots=np.zeros(self.max_cast_level)
                for i in range(1,self.max_cast_level+1):
                    spell_slots[i]=seeclassagain #add from database depending on level
                
    self.prepped_spells=spellist #user-defined, ensuring that they don't exceed slots (if it's a class that works that way) happens while choosing 
    self.current_spells=self.spell_slots #a list for counting how many spells remain. A short/long rest function will, among other things, set this equal to spell_slots again       
    
    def self.use_spell_slot(self,spell_level):
        self.current_spells[spell_level-1]-=1
        
    def self.apply_damage(self,damage):#accepts an integer to subtract from hp
        self.hp-=damage
        
    def self.canequip(self,equippable):#takes number of hands needed for each item from database
        if equippable#is shield or weapon:        
            if hands_in_use==2:
                return False
            elif hands_in_use<2:
                return True
        elif equippable#is armor:
            if #armor in equipped items:
                return False
            else:
                return True
                
    def self.equip_item(self,equippable):
        if self.canequip(equippable):
            self.equipped_items.append(equippable)
            equippable.equip()
        else:
           # UIdisplay("Can't equip!")
            #absolutely no idea how to do this
        
    def self.unequip_item(self,equippable):
        self.equipped_items.remove(equippable)
        equippable.unequip()
        
    def statline(self):  # Function creates a 6 element numpy array defining character's stat values
        stat = np.zeros(6)
        for i in range(6):
            a = random.randint(1, 7, size=4)
            droplow = np.sum(a) - np.min(a)
            stat[i] = droplow
        return stat

    def modifiers(self, stats):  # Takes in array of stats, return array of stat mods
        mods = np.zeros(6)
        for i in range(len(stats)):
            stat_mod = (stats[i] - 10) // 2
            mods[i] = stat_mod
        return mods

    def lvl(self, XP):
        xp = self.XP
        if (xp >= 0 and xp < 300):
            return 1
        elif (xp >= 300 and xp < 900):
            return 2
        elif (xp >= 900 and xp < 2700):
            return 3
        elif (xp >= 2700 and xp < 6500):
            return 4
        elif (xp >= 6500 and xp < 14000):
            return 5
        elif (xp >= 14000 and xp < 23000):
            return 6
        elif (xp >= 23000 and xp < 34000):
            return 7
        elif (xp >= 34000 and xp < 48000):
            return 8
        elif (xp >= 48000 and xp < 64000):
            return 9
        elif (xp >= 64000 and xp < 85000):
            return 10
        elif (xp >= 85000 and xp < 100000):
            return 11
        elif (xp >= 100000 and xp < 120000):
            return 12
        elif (xp >= 120000 and xp < 140000):
            return 13
        elif (xp >= 140000 and xp < 165000):
            return 14
        elif (xp >= 165000 and xp < 195000):
            return 15
        elif (xp >= 195000 and xp < 225000):
            return 16
        elif (xp >= 225000 and xp < 265000):
            return 17
        elif (xp >= 265000 and xp < 305000):
            return 18
        elif (xp >= 305000 and xp < 355000):
            return 19
        elif (xp >= 355000):
            return 20

    def proficiency(self, level):
        lvl = self.level
        if (lvl > 0 and lvl < 5):
            return 2
        if (lvl >= 5 and lvl < 9):
            return 3
        if (lvl >= 9 and lvl < 13):
            return 4
        if (lvl >= 13 and lvl < 17):
            return 5
        if (lvl >= 17):
            return 6
            
    def ability_score_improvement(self, userinput) # takes some form of user input to pull total allowed points addable from database and distribute them among stat scores
        self.stats+=userinput
        
    def self.add_xp(self,newxp):
        self.XP+=newxp
        self.level_up()
        
    def self.level_up(self):
        oldlevel=self.level
        self.level = self.lvl(self.XP)
        if self.level != oldlevel: #if level is updated, do all the level up things
            self.prof = self.proficiency(self.level)
            if self.level%4==0:
                self.ability_score_improvement(userinput)#takes user input here
                self.stat_mods = self.modifiers(self.stats)
            if self.magic_user==True:
                make_spell_slots()

Iain = newChar('human fighter')
print (Iain.XP)
print (Iain.level)
print (Iain.prof)
