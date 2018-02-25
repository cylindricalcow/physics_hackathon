# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:21:25 2018

@author: CammieFarruggio
"""
xp=2500
import numpy as np
xplist=np.array([300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000,195000,225000,265000,305000,355000])
levellist=np.arange(1,20)
if xp>2700:
    c,b,a=np.polyfit(xplist,levellist,2)
    level=np.floor(c*xp**2+b*xp+a)
    print(level)
else:
    b,a=np.polyfit(levellist,np.log(xplist),1)
    level=((np.log(xp)-a)/b)
    print(level)