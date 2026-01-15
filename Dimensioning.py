import numpy as np
#0-D array
a = np.array(32)
print(a)
#1-D array
b = np.array([1,2])
print(b)
#2-D array
c = np.array([[3,5],[6,7]])
print(c)
#3-D array
d = np.array([1,2,6,8],ndmin=3)
print(d)
print(d.ndim)