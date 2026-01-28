import numpy as np
#Convert the list into a NumPy array
arr = np.array([1,2,3,4,5])
print(arr)
#It shows the Container type
print(type(arr))
#Checking the version
print(f"Numpy Version:{np.__version__}")

"""Dimensioning"""
#0-D array
u = np.array(32)
print(u)
#1-D array
r = np.array([1,2])
print(r)
#2-D array
s = np.array([[3,5],[6,7]])
print(s)
#3-D array
t = np.array([1,2,6,8],ndmin=3)
print(t)
print(t.ndim)