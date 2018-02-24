import numpy as np
import numpy.random as random


class newChar:
    def __init__(self, raceclass, **kwargs):
        self.raceclass = raceclass
        self.stats = self.statline()  # Needs to be user defined. Use Kivy
        self.XP = 0
        self.level = 1

    def statline(self):  # Function creates a 6 element numpy array defining character's stat values
        stat = np.zeros(6)
        for i in range(6):
            a = random.randint(1, 7, size=4)
            droplow = np.sum(a) - np.min(a)
            stat[i] = droplow
        return stat


Iain = newChar('human fighter')
print (Iain.stats)
