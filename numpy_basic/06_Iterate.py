import numpy as np
#Iterating means going through elements one by one.
a = np.array([1,2,3,4])
for i in a:
    print(i)

#Iterating 2-D arrays
b = np.array([[1,2,3],[4,5,6]])
for x in b:
    for y in x:
        print(y)

"""nditer():It understands the layout of complex tables (arrays) and can do multiple jobs at once while walking through them.
whereas
we have to use n for loops  in case of for loops."""

c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in c:
  for y in x:
    for z in y:
      print(z)


for x in np.nditer(c):
    print(x)

#Iterating arrays with different data types
arr = np.array([1,2,3])
#op_dtypes stands for "Operand Data Types." It is a setting in nditer() that tells NumPy exactly what kind of data you want to see while you are looping through an array.
for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer.
    print(x)
#flags in nditer() are like extra instructions or "special powers" you give to the iterator to change how it behaves while moving through your data.

#Iterate with different step size
for x in np.nditer(b[:,::2]):
    print(b)

#Enumerated iteration using ndenumerate():Enumerated Iteration means looking at the values in an array while also keeping track of their exact location (the index or "address") at the same time.
#Enumeration on 1-D
ar = np.array([1, 2, 3])
for idx, x in np.ndenumerate(ar):
  print(idx, x)

#Enumeration on 2-D
f = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(f):
  print(idx, x)