# bar chart
# replace label

import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = range(len(movies)) # xs is range(5)
# plot bars with left x-coordinates [xs], 
# heights [num_oscars]

plt.bar(xs, num_oscars)
# label x-axis with movie names at bar centers

plt.xticks(xs, movies) # movies chage with xs
# alternatively, use the following to replace 
# the two lines above

plt.bar(xs, num_oscars, tick_label=movies)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
plt.show()
