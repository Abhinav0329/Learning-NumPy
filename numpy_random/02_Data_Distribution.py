from numpy import random
"""Data Distribution refers to a mathematical list of all possible values a random variable can take and how often they occur.
Instead of just generating "any" number, you use distributions to give your random data a specific shape or probability.
Such lists are important when working with statistics and data science."""

# random distribution is a mathematical rule that describes how likely different values are to occur. It defines the "shape" of your data.
# The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.
# 1-D array
x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=100)# 9 will never occur
print(x)

#2-D array
y = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print(y)

"""permutation is a random rearrangement of the elements in an array.
 It’s like shuffling a deck of cards: the items stay the same, but their order changes."""

#using shuffle():This modifies the original array directly.It returns None
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)# Use case: When you want to save memory and don't need to keep the original order.
print(arr)

#using permutation():This leaves the original array untouched and returns a new array that is shuffled
print(random.permutation(arr))#Use case: When you need to keep the original data in its specific order for later use.

"""Method	     Affects Original?   Returns Value?	            Best For...
 shuffle()	      Yes (In-place)	    No (None)	       Large datasets (memory efficient).
 permutation()	        No	           Yes (New array)	   When you need a "shuffled copy."""