
# Fig-7
# Title

import matplotlib.pyplot as plt
import numpy as np


city = ['Dhaka', 'Rajshahi', 'Borishal', 'Khulna']
population1 = [10.4, 6.7, 8.9, 15.2]
population2 = [11.2, 7.5, 9.7, 16.0]
population3 = [12.0, 8.3, 10.5, 16.8]
population4 = [12.8, 9.1, 11.3, 17.6]
population5 = [13.6, 9.9, 12.1, 18.4]
population6 = [14.4, 10.7, 13.9, 19.2]

figure = plt.figure(figsize=(8, 3), facecolor='w')

# Add Title
plt.title("Title Bar", color='magenta', fontsize=17, fontweight='bold', style='italic')
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

figure.patch.set_alpha(1) # set_alpha() background color


plt.plot(city, population1, color='red', marker='s', linestyle='solid')
plt.plot(city, population2, color='green', marker='X', linestyle='dotted')
plt.plot(city, population3, 'b^-.')
plt.plot(city, population4, 'm*-', color="black")
plt.plot(city, population5, color='green', marker='x', linestyle='dotted')
'''
# use format string to specify color, marker, and line style ('color marker linestyle')
plt.plot(city, population1, 'rs--')
plt.plot(city, population2, 'gX', linestyle='dotted')
plt.plot(city, population3, 'b^-.')
plt.plot(city, population4, 'm*-', color="black")
'''
# plot(X, Y, 'color pointShape')
 
# matplotlib.pyplot.show()