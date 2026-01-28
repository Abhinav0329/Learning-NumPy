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
new_arr = d.reshape(2, 3, 2)
print(new_arr)#outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

"""
Condition for reshaping:
->Yes, as long as the elements required for reshaping are equal in both shapes.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(3, 3)
print(newarr)
-->Error:we cannot convert 1D array with 8 elements into 2D array with 3 elements in each dimension."""

#Checking the whether the returned array is Copy or View
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
"""When you use .reshape(), it doesn't waste memory by making a copy of the numbers. 
It just points back to the original array (arr). Since the reshaped array is "borrowing" from arr, 
printing the .base shows you that original source."""

#Passing unknown dimension(You are allowed to have one "unknown" dimension),NumPy will calculate this number for you.
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newar = ar.reshape(2, 2, -1)#NumPy calculates -1 automatically becomes 2 columns.
print(newar)

#Flattening the arrays:It means converting a multidimensional array into a 1D array.
r = np.array([[1, 2, 3], [4, 5, 6]])
newr = r.reshape(-1)
print(newr)