import numpy as np

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

#Checking the Data Types
a = np.array([1,2,3,4,5])
print(a.dtype)

#Creating array with defined Data Types
b = np.array([12,16,45],dtype = "f")
print(b)

#Converting Data Types
arr = np.array([19.1,24.2,4.5])
new_arr = arr.astype('i')#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
print(new_arr)

c = np.array([1,0,3])
new_c = c.astype(bool)
print(new_c)

"""
ValueError->It is an error that occurs when a function gets an argument that is the right type but an invalid value
Given code gives error:
-->error = np.array(['a',2,6],dtype='i')
-->print(error)
"""