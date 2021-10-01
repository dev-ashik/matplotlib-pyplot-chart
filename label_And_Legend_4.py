
# Fig-8
# Label and location
# add legend


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
# Title
plt.title("Title Bar", color='magenta', fontsize=17, fontweight='bold', style='italic')
                                # figsize=(X, Y)
'''
location as loc
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

figure.patch.set_alpha(1) # set_alpha() background color

 #__________________________________

plt.plot(city, population1, 'rs--', label="Year1947")
plt.plot(city, population2, 'gX', linestyle='dotted', label="Year1971")
plt.plot(city, population3, 'b^-.', label='Year2001')
plt.plot(city, population4, 'm*-', color="black", label='Year2020')


# lebel locaton
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1)) # label decoretion
                                #bbox_to_anchor=(X, Y)
# plot(X, Y, 'color pointShape')

 #__________________________________
'''
plt.plot(city, population1, 'rs--')
plt.plot(city, population2, 'gX', linestyle='dotted')
plt.plot(city, population3, 'b^-.')
plt.plot(city, population4, '*-', color="black")

plt.legend(['Year1947', 'Year1971', 'Year2001', 'Year2020'])
'''
 #__________________________________
# matplotlib.pyplot.show()