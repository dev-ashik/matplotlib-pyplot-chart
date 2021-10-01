
# Fig-2

import matplotlib.pyplot
#import numpy


city = ['Dhaka', 'Rajshahi', 'Borishal', 'Khulna']
population1 = [10.4, 6.7, 8.9, 15.2]
population2 = [10.8, 7.1, 9.3, 15.6]
population3 = [11.2, 7.5, 9.7, 16.0]
population4 = [11.6, 7.9, 10.1, 16.4]
population5 = [12.0, 8.3, 10.5, 16.8]
population6 = [12.4, 8.7, 10.9, 17.3]

figure = matplotlib.pyplot.figure(figsize=(8, 3), facecolor='w')
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

'''

figure.patch.set_alpha(.8) # set_alpha() background color
 #__________________________________

matplotlib.pyplot.plot(city, population1, 'r')
matplotlib.pyplot.plot(city, population2, 'g')
matplotlib.pyplot.plot(city, population3, 'y')
matplotlib.pyplot.plot(city, population4, 'b')
matplotlib.pyplot.plot(city, population5, 'wo', color='red')
matplotlib.pyplot.plot(city, population6, color="black")
# plot(X, Y, 'color pointShape')
 
 #__________________________________
# matplotlib.pyplot.show()