import numpy as np
a = np.array([1,2,3,4,5,6])
b = np.array_split(a,3)#Allows you to split an array into equal sections if the array size is perfectly divisible by the number of splits requested.
print(b)#The return value is a list containing three arrays.

#Accessing arrays from b.
print(b[0])
print(b[1])
print(b[2])

#If the array has less elements than required.
c = np.array_split(a,4)
print(c)

"""The standard split() function will crash if you try to divide an array into parts that aren't perfectly equal, 
array_split() handles unequal divisions gracefully."""

d = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
new_d = np.array_split(d,3)
print(new_d)#returns three 2-D arrays.

e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_e = np.array_split(e,3)
print(new_e)

"""Either we can specify axis or use hsplit()/vsplit to split.
Function	        Equivalent to...	
hsplit(arr, n)	split(arr, n, axis=1)
vsplit(arr, n)	split(arr, n, axis=0)"""

# hsplit() (Horizontal Split):meaning it cuts along the vertical axis (columns)
matrix1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
# Split into 2 parts along the columns
left, right = np.hsplit(matrix1, 2)
print(left,right)

#vsplit() (Vertical Split):means it cuts the array along the horizontal axis (rows).
matrix2 = np.array([[1, 2],
                   [3, 4],
                   [5, 6],
                   [7, 8]])
# Split into 2 parts along the rows
top, bottom = np.vsplit(matrix2, 2)
print(top,bottom)