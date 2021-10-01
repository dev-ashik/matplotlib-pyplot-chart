
# Fig-4 line-style

import matplotlib.pyplot as plt
import numpy as np


city = ['Dhaka', 'Rajshahi', 'Borishal', 'Khulna']
population1 = [6.7, 6.7, 6.7, 6.7]
population2 = [11.2, 7.5, 9.7, 16.0]
population3 = [12.0, 8.3, 10.5, 16.8]
population4 = [12.8, 9.1, 11.3, 17.6]
population5 = [13.6, 9.9, 12.1, 18.4]
population6 = [14.4, 10.7, 12.9, 19.2]
population7 = [15.2, 11.5, 13.7, 20.0]
population8 = [16.0, 12.3, 14.5, 20.8]
population9 = [16.8, 13.1, 15.3, 21.6]

figure = plt.figure(figsize=(8, 3), facecolor='w')
                                # figsize=(X, Y)
'''
color code
green => g
red => r
yellow =>y
black =>
blue => b
white => w
magenta => m
c

color='black'
color='green'

'''

figure.patch.set_alpha(.8) # set_alpha() background color
 #__________________________________
'''
plt.plot(city, population2, color='green', linestyle='dotted')
plt.plot(city, population4, color="c", linestyle='solid')


'''
 #__________________________________
 
# use format string to specify color, marker, and line style ('color marker linestyle')

plt.plot(city, population1, 's--', color='r')
plt.plot(city, population2, 'o:', color='blue')  #linestyle='dotted'
plt.plot(city, population3, '^-', color='m')
plt.plot(city, population4, 'v-.', color='c')  #linestyle='solid'
plt.plot(city, population5, '+', color='red')
plt.plot(city, population6, '*', color='blue')
plt.plot(city, population7, '.', color='green')
plt.plot(city, population8, '<', color='black')
plt.plot(city, population9, '>', color='m')

 #__________________________________
# plot(X, Y, 'color pointShape')
 
# matplotlib.pyplot.show()