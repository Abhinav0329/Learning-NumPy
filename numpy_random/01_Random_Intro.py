#Generating random number
from numpy import random
x = random.randint(100)
print(x)

#Generating random float
y = random.rand()# rand() method returns a random float between 0 and 1
print(y)

#Generating random array
z = random.randint(100,size=(5))# randint() method takes a size parameter where you can specify the shape of an array.
print(z)

w = random.randint(100,size=(3,5))# 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
print(w)

a = random.rand(5)# 1-D array containing 5 random floats:
print(a)

b = random.rand(3,5)# 2-D array with 3 rows, each row containing 5 random numbers
print(b)

#Generating random number from array
c = random.choice([3,6,8,2])# it is function that selects random elements from an existing array.
print(c)
d = random.choice([3,4,6,8,9,2],size =(3,5))# 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
print(d)