# barh chart
'''

import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]


plt.barh(movies, num_oscars)
plt.xlabel("# of Academy Awards")
plt.title("My Favorite Movies")
'''
import random
def coinToss():
    return random.randint(0, 1)

recordList = []

for j in range(10**5):

    for i in range(100):
        flip = coinToss()
        if (flip == 0):
            recordList.append(0)

print(str(recordList.count(0)))
print(recordList)


