import numpy as np
"""Filtering is simply the process of extracting specific elements from an existing array and creating a new array out of them.
In NumPy, you filter arrays using a Boolean Indexing List. A boolean list is just a list of True and False values that corresponds to the indices of your array."""

#The Manual Boolean Mask (The "Hand-Pick" Method)
a = np.array([10, 20, 30, 40])
# We only want the first and last elements
mask = [True, False, False, True]
new_a = a[mask]
print(new_a)

#Creating a Filter with a Condition (The "Smart" Method)
b = np.array([5, 12, 18, 25, 30])
condition = b > 15
# This creates the mask: [False, False, True, True, True] automatically!
result = b[condition]
print(result)

#Filtering with Multiple Conditions (The "Advanced" Method)
c = np.array([10, 15, 20, 25, 30])
# I want numbers bigger than 12 AND smaller than 28
mask = (c > 12) & (c < 28)
print(c[mask])