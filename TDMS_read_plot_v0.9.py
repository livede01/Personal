# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nptdms import TdmsFile
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import time

starttime = time.time()
pfad = r'C:\Temp\#2_x-y=0.5mm' # r=raw. No decoding of '\'

firstRun = True
for filename in glob.glob(pfad + r'\*.tdms'):
    print(filename)
    tdms_file = TdmsFile(filename)
    datachannel = tdms_file.object('DataNibbles', 'Value')
    angleSamples = np.array(datachannel.data)
    angleMean = angleSamples.mean()
    root = tdms_file.object()
    xPosPoint = np.array(root.property('Position X (mm)'))
    
    if firstRun:
        firstRun = False
        angle = np.array(angleMean)
        xPos = np.array(xPosPoint)
    else:
        angle = np.append(angle,angleMean)
        xPos = np.append(xPos,xPosPoint)

plt.plot(xPos, angle)

title = 'KMA310 before 30mm bar magnet (mid-track)'
plt.title(title)
plt.xlabel('Position [mm]')
plt.ylabel('Angle[LSB]')
#plt.figlegend(['0.5mm', '1.5mm','2.5mm','3.5mm','4.5mm'], 'upper right')
#plt.legend(['0.5mm', '1.5mm','2.5mm','3.5mm','4.5mm'], bbox_to_anchor=(1, 1), loc=4, borderaxespad=0)
# =============================================================================
# Possbile positions of the legend:
# upper right 	1
# upper left  	2
# lower left   	3
# lower right 	4
# right 	       5
# center left 	6
# center right 	7
# lower center 	8
# upper center 	9
# center 	10
# =============================================================================

plt.show()
#plt.savefig(title + '.png')

stoptime = time.time()
duration = stoptime - starttime
print(duration)