# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:49:30 2021

@author: ashik
"""

import matplotlib.pyplot as plt
import numpy as np

# x & y data
Statesuniont = ['Delhi', 'Surat', 'Kolkata', 'Mumbai', 'Assam', 'Bihar']
population = [1.9, 0.44, 0.45, 1.84, 3.00, 9.9]
population2 = [2.2, 1.30, 5.00, 7.84, 3.00, 2.9]
population3 = [7.9, 9.44, 2.45, 7.84, 8.00, 0.9]

figure = plt.figure(facecolor='g', figsize=(8, 3))
figure.patch.set_alpha(.5)

#figure.suptitle("States and Union Territory p\Population Chart", color='r', fontsize=10, fontweight='bold', style='italic')

# plt.title("Population Graph", color='magenta', fontsize=15, fontweight='bold', style='italic')

# first graph
    #plt.subplot(4, 2, 1)
plt.title("Bar Chart", color='magenta', fontsize=15, fontweight='bold', style='italic')

#plt.grid(linestyle='-', linewidth=.5, color='r', axis='y')


'''
b => blue
g => green
m => parple

^ => triangle
s => squre

- => line
-- => dote dote line
-. => -.-.- line

color='magenta'
fontsize=15
fontweight='bold'
style='italic'
facecolor='g'

grid
linestyle='-'
linewidth=.3
color='r'
axis='y'
axis='x'

plt.pie(population) # sercle

plt.legend
    best
	upper right
	upper left
	lower left
	lower right
	right
	center left
	center right
	lower center
	upper center
	center
'''

# plt.plot(Statesuniont, population)
# plt.plot(Statesuniont, population, 'b^')
# plt.plot(Statesuniont, population, 'g^-.') # ('color, pointIndicator, lineStyle')
plt.plot(Statesuniont, population, 'gs-.', label="population")
plt.legend(loc='upper right', bbox_to_anchor=(1.1, -0.5))

plt.plot(Statesuniont, population2, 'gs-.', label="population")
plt.plot(Statesuniont, population3, 'gs-.', label="population")

plt.ylabel("<------Population------>", color='r', fontsize=10, fontweight='bold')
plt.xlabel("<------States & Union Territory------->", color='b', fontsize=4, fontweight='bold')
#plt.yticks(color='r', fontsize=6)
plt.yticks(color='r') 
plt.xticks(color='b')

# second graph
#plt.subplot(4, 2, 2) # (long, height, quantity)
    # plt.plot(Statesuniont, population, 'gs-.')
#plt.pie(population) # sercle


plt.show()