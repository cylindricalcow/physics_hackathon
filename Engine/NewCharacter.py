import game_functions as game
import numpy as np
import numpy.random as random


class newChar:
    def __init__(self, raceclass, **kwargs):
        self.raceclass = raceclass
        self.stats = self.statline()  # Needs to be user defined. Use Kivy
        self.stat_mods = self.modifiers(self.stats)
        self.XP = 0
        self.level = self.lvl(self.XP)
        self.prof = self.proficiency(self.XP)
        # Dummy code, the dice command depends on a character's raceclass
        self.hp = game.dice(8) + self.stat_mods[3]
        # dice roll will be dependent on weapon attack values in database
        self.weapon_damage = self.proficiency(self.level)+self.stat_mods[1]+game.dice(8)

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


Iain = newChar('human fighter')
print (Iain.XP)
print (Iain.level)
print (Iain.prof)
