# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:21:25 2018

@author: CammieFarruggio
"""
import numpy as np
"""level = log(a(exp(bx)))=log(a)+bx  where a and b are constants and x is xp
we know the highest xp that corresponds to each level, so if we solve for a and b of the
linear equation and then take the floor of the level which this linear function gives for
any xp this should give the appropriate character level"""
xplist=[300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000,195000,225000,265000,305000,355000]
levellist=np.arange(1,20)
print(np.polyfit(xplist,levellist,1))