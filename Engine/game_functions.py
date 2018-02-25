import numpy as np
import numpy.random as random
import operator

def dice(number_dice, nsides):  # Takes in an int, returns roll on n-sided die
    rolled = 0
    for die in range(number_dice):
        roll=random.randint(1, nsides+1)
        rolled+=roll 
    return rolled


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
    
def Initiative_Order(rolls): #Takes in dict, returns initiative order
    sorted_x = sorted(rolls.items(), key=operator.itemgetter(1))[::-1]
    #sorted(rolls.items(), key= lambda (k,v1):v2)
    #print (OrderedDict(sorted(rolls.items(),key=lambda (k, v:v[1]) ))
    players=[]
    for player_init in sorted_x:
        players.append(player_init[0])
    return players


def save_throw(stat, adv=False, disadv=False, proficiency=False): #Takes in stat, additional parameters for adv/disadv effects, and for proficiency
	if proficiency:
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
 
def distance(player,target):
    deltax=target.position[0]-player.position[0]
    deltay=target.position[1]-player.position[1]
    distance=(deltax**2+deltay**2)**(1/2)
    return(distance)