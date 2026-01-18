import numpy as np
#The shape of an array is the number of elements in each dimension.
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
"""(2, 3), which means outermost dimension will have 2 arrays, each with 3 elements:"""

#Level upto 5-Dimensions
b = np.array([1,2,3,4],ndmin=5)
print(b)
print("Shape of array",b.shape)
"""The 4 represents the four elements in your list.
The 1s represent the "empty" dimensions added to satisfy the ndmin=5 rule."""

#Reshaping the array(1-D->2-D)
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = c.reshape(4,3)
print(newarr)

#Reshaping the array(1-D->3-D)
d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = d.reshape(2, 3, 2)
print(newarr)#outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

"""
Condition for reshaping:
->Yes, as long as the elements required for reshaping are equal in both shapes.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(3, 3)
print(newarr)
-->Error:we cannot convert 1D array with 8 elements into 2D array with 3 elements in each dimension."""
