import game_functions as game
import numpy as np
import numpy.random as random


class Character:
    def __init__(self, raceclass='human fighter',new_player=False, **kwargs):
        self.raceclass = raceclass
        if new_player:
        #in stats/stat_mods, index 0-5 correspond to STR, DEX, CON,INT, WIS, and CHA respectively            
            self.position = [0.0, 0.0] #x and y coordinates; pull from database
            self.art=databaseart#this is gonna come from the database eventually            
            self.stats = self.statline()  # Needs to be user defined. Use Kivy
            self.stat_mods = self.modifiers(self.stats)
            self.ac=10+self.stat_mods[1]#+ac of equipped armor
            self.XP = 0
            self.speed=30#-slow effect from armor #dummy values : will pull from database
            self.level = self.xp2level(self.XP)
            self.prof = self.proficiency(self.level)
        # Dummy code, the dice command depends on a character's raceclass
            self.hp = game.dice(self.level,8) + self.stat_mods[2]
            self.items=[]#again: starting items? class-dependent?
            self.equipped_items=[]
            self.available_actions=[]
            self.available_bonus_actions=[]
            self.dodging=False
        # dice roll will be dependent on weapon attack values in database
            self.weapon_damage = self.proficiency(self.level)+self.stat_mods[0]+game.dice(8)
            self.magic_user=False #depeding on class info from database
            if self.magic_user:
                make_spell_slots
            #Conditions      
            self.paralyzed=False 
            self.poisoned=False
            self.healthremoval=False
            self.grappled=False
            self.prone=False
            self.petrified=False
            self.restrained=False
            self.advantageagainst=False
            self.moveslow=False   
          ######################END INIT  
    def getspeed(self):
        if(self.grappled==True or self.petrified==True or self.restrained==True):
            return 0
        if(self.moveslow==True or self.prone==True):
            return self.speed/2
        return self.speed
        
    def restrained(self):
        self.restrained==True
        
        
        
    #############################BEGIN GETTERS  
    def get_str(self):
        return self.stats[0]
    def get_dex(self):
        return self.stats[1]
    def get_con(self):
        return self.stats[2]
    def get_int(self):
        return self.stats[3]
    def get_wis(self):
        return self.stats[4]
    def get_cha(self):
        return self.stats[5]
    def get_strmod(self):
        return self.mods[0]
    def get_dexmod(self):
        return self.mods[1]
    def get_conmod(self):
        return self.mods[2]
    def get_intmod(self):
        return self.mods[3]
    def get_wismod(self):
        return self.mods[4]
    def get_chamod(self):
        return self.mods[5]
    ##############################END GETTERS
    ##############################BEGIN SETTERS
    def set_strmod(self, value):
        self.mods[0]=value
    def set_dexmod(self, value):
        self.mods[1]=value
    def set_conmod(self, value):
        self.mods[2]=value
    def set_intmod(self, value):
        self.mods[3]=value
    def set_wismod(self, value):
        self.mods[4]=value
    def set_chamod(self, value):
        self.mods[5]=value
    ##############################END SETTERS

    def make_spell_slots(self):   
        self.max_cast_level=seeclass #add from database depending on level
        self.cantrips=seeclass#again, add from database depending on class/level
        self.spell_slots=np.zeros(self.max_cast_level)
        for i in range(1,self.max_cast_level+1):
            spell_slots[i]=seeclassagain #add from database depending on level
                
    self.prepped_spells=spellist #user-defined, ensuring that they don't exceed slots (if it's a class that works that way) happens while choosing 
    self.current_spells=self.spell_slots #a list for counting how many spells remain. A short/long rest function will, among other things, set this equal to spell_slots again       
    
    def use_spell_slot(self,spell_level):
        self.current_spells[spell_level-1]-=1
        
    def apply_damage(self,damage):#accepts an integer to subtract from hp
        self.hp-=damage
        
    def canequip(self,equippable):#takes number of hands needed for each item from database
        
        if type(equippable) != Equippable:
            return False
        elif (type(equippable)==Weapon) or (type(equippable)==Shield):
            if self.hands_free<equippable.hands_used:
                return False
            else:
                return True
        elif type(equippable)==Armor:
            for i in range(len(self.equipped_items)):
                if type(self.equipped_items[i])==Armor:
                    return False
                
    def equip_item(self,equippable):
        if self.canequip(equippable):
            self.equipped_items.append(equippable)
            equippable.equip()
        else:
           # UIdisplay("Can't equip!")
            #absolutely no idea how to do this
            pass
        
    def unequip_item(self,equippable):
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

    def xp2level(xp): #Takes in experience points, returns character level 
        xplist=np.array([0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000,195000,225000,265000,305000,355000])
        levellist=np.arange(1,21)   
        if xp < 2700: 
            level = np.log(3*xp/100)/np.log(3)
        else:
            a,b,c=np.polyfit(levellist,xplist, 2)
            level = (-b+np.sqrt(np.power(b,2)-4*a*(c-xp)))/(2*a) #Fitting to quadratic above level 4. Not perfect, but functional
        return np.floor(level) 

    def proficiency(self, level):
        lvl = self.level
        prof=np.floor(lvl/4+2)
        return prof
            
    def ability_score_improvement(self, userinput): # takes some form of user input to pull total allowed points addable from database and distribute them among stat scores
        self.stats+=userinput
        
    def add_xp(self,newxp):
        self.XP+=newxp
        self.level_up()
        
    def level_up(self):
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
