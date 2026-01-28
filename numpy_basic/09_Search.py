import numpy as np

"""The "Choose" Method(Three arguments)
You provide a condition, a value to use if the condition is True, and a value to use if it is False.
Syntax: np.where(condition, value_if_true, value_if_false)"""
scores = np.array([45, 78, 22, 90, 55])
# If score >= 50, "Pass", else "Fail"
results = np.where(scores >= 50, "Pass", "Fail")
print(results)

"""The "Find" Method (One Argument)
If you only provide the condition, 
NumPy returns the indices (coordinates) where the condition is True"""
a = np.array([10, 20, 30, 40, 50])
# Find indices where elements are greater than 35
indices = np.where(a > 35)
print(indices)# (Meaning indices 3 and 4 match the condition)

#Accessing those indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#Accessing those indexes where the values are odd
y = np.where(arr%2 == 1)
print(y)

"""function used to find the indices where elements should be inserted into an array to maintain its sorted order
It does not actually insert the elements; it just tells you the "slot" where they belong. 
It uses binary search, which makes it extremely fast (O(log(n)) complexity)
It starts their searching from left side by default."""
# Note: The input array MUST be sorted
ar = np.array([10, 20, 30, 40, 50])
index1 = np.searchsorted(ar, 35)
print(index1)

"""The main difference between side='left' and side='right' only becomes visible when the value you are searching for already exists in the array
If the value is not in the array,both settings return the same index."""

"""  Setting	         Behavior with Existing Values	                     Resulting Index
   side='left'	     Finds the first occurrence of the value.	The index of the first matching element
   side='right'	     Finds the last occurrence of the value.	The index after the last matching element"""

"""side='left' gives you the index i such that ar[i-1] < v <= ar[i].
side='right' gives you the index i such that ar[i-1] <= v < ar[i]."""

# Array with duplicate values
ar = np.array([10, 20, 20, 20, 30])
left_idx  = np.searchsorted(ar, 20, side='left')
right_idx = np.searchsorted(ar, 20, side='right')
print(f"Left side: {left_idx}")   # Output: 1
print(f"Right side: {right_idx}") # Output: 4

b = np.array([1, 3, 5, 7])
z = np.searchsorted(b, [2, 4, 6])
print(z)