import numpy as np
import numpy.random as random


def dice(n):  # Takes in an int, returns roll on n-sided die
    return random.randint(1, n + 1)


# Takes in Hit Bonus and armor class, returns True if you hit
def hit(To_Hit_Bonus, Armor_Class, adv=False, disadv=False):
    # Additional paramaters defined to account for advantage/disadvantage effects
    attack_roll = d20(adv, disadv) + To_Hit_Bonus
    if attack_roll >= Armor_Class:
        adv = False
        disadv = False
        return True
    adv = False
    disadv = False
    return False


def d20(adv=False, disadv=False):  # Gives roll on 20-sided die
    # Advantage takes the better of two rolls
    # Disadvantage takes worse of two rolls
    a = random.randint(1, 21)
    b = random.randint(1, 21)
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


def initiative(dex, adv=False, disadv=False):
	#Function takes in dex, additional parameters for adv/disadv effects
    init = d20(adv, disadv) + dex
    adv = False
    disadv = False
    return init


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