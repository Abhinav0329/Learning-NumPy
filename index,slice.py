import numpy as np
#Accessing 1-D arrays
a = np.array([1,2,3,4])
print(a[0])
#Accessing 2-D arrays
b = np.array([[1,2,4],[2,3,4]])
#To access elements from 2-D arrays we can use comma-separated integers representing the dimension and the index of the element.
print(b[1,1])
#Acessing 3-D arrays
c = np.array([[[1,2,3],[59,54,2]],[[23,43,65],[8,56,85]]])
print(c[1,0,2])

#Negative-indexing
d = np.array([[1,2,3,4],[9,8,5,7]])
print("Last element from 2nd dim:",d[1,-1])

# Slicing->[start:end:step]
arr = np.array([1,2,3,4,5,6,7,8,9,])
print(arr[5:])#Slice elements from index 5 to the end of the array
print(arr[:5])#Slice elements from the beginning to index 5 (not included)
print(arr[:])#slice entire array
print(arr[::-1])#slice entire array after reversing it

#2-D Slicing
e = np .array([[13,2,4,7],[23,4,5,6]])
print(e[0,1:4])
print(e[0:2,1:3])
print(e[0:2,3])