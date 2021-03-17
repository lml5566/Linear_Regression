# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:22:25 2021

@author: lml5566
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
raw = pd.read_csv('E:\CP\exam\map.csv',encoding='big5') 
y=raw['RO']
x=raw['Spd']
plt.scatter(x,y)

plt.xlabel('Spd%')
plt.ylabel('RO%')

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='red')
print(np.corrcoef(x, y))

plt.figure()
y2=raw['RO']
x2=raw['Psb']
plt.scatter(x2,y2)

plt.xlabel('Psb')
plt.ylabel('RO%')

plt.plot(np.unique(x2), np.poly1d(np.polyfit(x2, y2, 1))(np.unique(x2)), color='red')
print(np.corrcoef(x2, y2))
