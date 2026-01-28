import numpy as np
from numpy.ma.core import concatenate

a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b # Vector Addition performed by the numpy library in your code.
print(c)

new_arr = np.concatenate((a,b))# It is used to join a sequence of arrays along an existing axis or simply attaches the lists to each other.
print(new_arr)

d = np.array([[1,2,3],[4,5,6]])
e = np.array([[7,8,9],[10,11,12]])
new_ar = np.concatenate((d,e),axis=1)
print(new_ar)

"""In both stack() and concatenate(),if axis is not explicitly passed, it is taken as 0."""

st_arr = np.stack((a,b),axis=1)# stack() joins arrays by creating a new dimension
print(st_arr)

#using hstack()
hst_ab = np.hstack((a,b))
print(hst_ab)

#using vstack()
vst_ab = np.vstack((a,b))
print(vst_ab)

#using dstack()
dst_ab = np.dstack((a,b))
print(dst_ab)