# fig-3
# marker

import matplotlib.pyplot as plt
import numpy as np


city = ['Dhaka', 'Rajshahi', 'Coxesbazar', 'Chitagong']
population1 = [10.4, 6.7, 8.9, 15.2]
population2 = [11.2, 7.5, 9.7, 16.0]
population3 = [12.0, 8.3, 10.5, 16.8]
population4 = [12.8, 9.1, 11.3, 17.6]
population5 = [13.6, 9.9, 12.1, 18.4]
population6 = [14.4, 10.7, 12.9, 19.2]
population7 = [15.2, 11.5, 13.7, 20.0]
population8 = [16.0, 12.3, 14.5, 20.8]
population9 = [16.8, 13.1, 15.3, 21.6]
population10 = [17.6, 13.9, 16.1, 22.3]




figure1 = plt.figure()

figure1.set_alpha(.8)

'''
marker

marker='s'
marker='o'
marker='^'
marker='v'
marker='+'
marker='*'
marker='.'
marker='<'
marker='>'

'''
 #__________________________________

# use format string to specify color, marker, and line style
plt.plot(city, population1, color='green', marker='|')
plt.plot(city, population2, color='r', marker='s')
plt.plot(city, population3, color='blue', marker='o')
plt.plot(city, population4, color='m', marker='^')
plt.plot(city, population5, color='c', marker='v')
plt.plot(city, population6, color='red', marker='+')
plt.plot(city, population7, color='blue', marker='*')
plt.plot(city, population8, color='green', marker='.')
plt.plot(city, population9, color='black', marker='<')
plt.plot(city, population10, color='m', marker='>')

 #__________________________________


'''
# use format string to specify color, marker, and line style
plt.plot(city, population1, 's', color='r')
plt.plot(city, population2, 'o', color='blue')
plt.plot(city, population3, '^', color='m')
plt.plot(city, population4, 'v', color='c')
plt.plot(city, population5, '+', color='red')
plt.plot(city, population6, '*', color='blue')
plt.plot(city, population7, '.', color='green')
plt.plot(city, population8, '<', color='black')
plt.plot(city, population9, '>', color='m')
'''
 #__________________________________