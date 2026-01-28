import numpy as np
a = np.array([11,22,34,42])
b = a.copy()
"""A Copy is a completely new array with its own dedicated memory. 
It is a physical duplication of the data."""
a[1]=43
print(a)
print(b)#The copy SHOULD NOT be affected by the changes made to the original array.

c = np.array([1,2,3,4])
d = c.view()
"""A View is a new array object that looks at the same memory buffer as the original array.
It is essentially a "window" into the original data."""
c[2]=47
print(c)
print(d)#The view SHOULD be affected by the changes made to the original array.

""" Feature           	        View	                      Copy
Data Ownership	     Shares data with the original	    Owns its own data
Memory Usage	     Very low (minimal overhead)	    High (duplicate of data)
Modification	     Affects the original array	       Does NOT affect the original
Commonly created by	   Basic slicing (a[1:5])	       .copy() or Fancy Indexing (a[[0,2]])"""

#Checking if array owns its data
arr = np.array([1,2,3,4,5,6])
x = arr.copy()
y = arr.view()
print(x.base)#returns None if the array owns the data.
print(y.base)#Otherwise, the base  attribute refers to the original object.