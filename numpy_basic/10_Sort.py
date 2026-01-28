import numpy as np
"""This function returns a sorted copy of an array. 
It does not change the original array unless you call it as a method
-->Syntax: np.sort(a, axis=-1, kind=None, order=None)<--
->1D Arrays: Simply puts numbers in ascending order.
->2D Arrays (Matrices): You must specify the axis.
axis=0: Sorts each column independently.
axis=1: Sorts each row independently (default)"""

a = np.array([3, 1, 5, 2, 4])
sorted_a = np.sort(a)
print(sorted_a)

"""argsort returns the indices that would sort the array. 
This is incredibly useful when you need to sort one array based on the values of another (like sorting a list of names based on ages)."""
prices = np.array([100, 50, 75])
items  = np.array(["TV", "Phone", "Radio"])
# Get the indices that would sort the prices
indices = np.argsort(prices)
print(indices)
# Output: [1, 2, 0] (Index 1 is the smallest price, then 2, then 0)
# Use those indices to sort the items
print(items[indices])
"""Note-->1.Descending Order:NumPy doesn't have a reverse=True parameter. 
To sort in descending order, you simply flip the sorted array: np.sort(arr)[::-1]
2.In-place Sorting:If you want to sort the original array to save memory: arr.sort() 
(This modifies arr and returns None)."""

#Sorting 2-D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))