import numpy as np
import numpy.random as random


def dice(n):  # Takes in an int, returns roll on n-sided die
    return random.randint(1, n + 1)


# Takes in Hit Bonus and armor class, returns True if you hit
def hit(To_Hit_Bonus, Armor_Class, adv=False, disadv=False):
    # Additional paramaters defined to account for advantage/disadvantage effects
    attack_roll = d20(adv, disadv) + To_Hit_Bonus
    if attack_roll >= Armor_Class:
        return True
    else:
        return False


def d20(adv=False, disadv=False):  # Gives roll on 20-sided die
    # Advantage takes the better of two rolls
    # Disadvantage takes worse of two rolls
    a = dice(20)
    b = dice(20)
    if adv and disadv:
        adv = False
        disadv = False
    if adv:
        if a > b:
            return a
        else:
            return b
    if disadv:
        if a > b:
            return b
        else:
            return a
    return a


def initiative_roll(dex, adv=False, disadv=False):
    #Function takes in dex, additional parameters for adv/disadv effects
    init = d20(adv, disadv) + dex
    return init
    
def initiative_order(roll_dict):#accepts a dict with playernames as keys referencing integer values of initiative rolls
    turn_order=[]#an ordered list with the names of characters in order of turns    
    rollslist=list(set(roll_dict.values())
    rollslist.sort()
    rollslist=list(reversed(rollslist))
    for i in range(len(rollslist)):
        for key in roll_dict.keys():
            if roll_dict[key]==rollslist[i]:
                turn_order.append(key)
    return(turn_order)
    


def save_throw(stat, adv=False, disadv=False, proficiency=False): #Takes in stat, additional parameters for adv/disadv effects, and for proficiency
	if prof:
		return d20(adv, disadv)+stat+proficiency
	else:
		return d20(adv, disadv)+stat


def statline(): #Function creates a 6 element numpy array defining character's stat values
	stat=np.zeros(6)
	for i in range(6):
		a=random.randint(1,7,size=4)
		droplow = np.sum(a)-np.min(a)
		stat[i] = droplow
	return stat
 
 def calclevel(xp):#function takes a current xp value and gives a current player level
     import numpy as np
     xplist=[300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000,195000,225000,265000,305000,355000]
     levellist=np.arange(1,20)
     if xp>6500:
         c,b,a=np.polyfit(xplist,levellist,2)
         level=np.floor(c*xp**2+b*xp+a)
         return(level)
    else:
        b,a=np.polyfit(xplist,levellist,1)
         level=np.floor(b*xp+a)
         return(level)