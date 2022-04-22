# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 08:33:04 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

# ************************
# Aula 17
# ************************

'''
COMANDOS GIT

git revert ____
git reset ____
git branch ____
'''
# ************************

import json
file_path = 

try:

except:

# ************************

lambda

# ************************

map(func, iter1)

# ************************

filter(function, iterable)

# ************************

class

# ************************

'''
NUMPY
NumPy is the fundamental package needed for scientific computing with Python

Numpy Features:
- Typed multidimensional arrays (vector, matrices)
- Fast numerical computations (matrix math)
- High-level math functions
- Open Source 
'''

import numpy as np

print(np.__version__)
print(np.version)

# Ctrl - I = Getting help

'''
ARRAYS

Arrays are a homogeneous collection of exactly the same data-type
Arrays can have any number of dimensions, including zero (a scalar).
Arrays are typed: np.uint8, np.int64, np.float32, np.float64

Array Attributes: 

      students.shape        #(2, 2, 3)  2 blocks, 2 lines, 3 elements
      students.nbytes       # 12  shape *itemsize
      students.ndim         # 3  dimension 
      students.dtype        # int8   data type
      students.size         # 12   elements 
      students.data         #<memory at 0x00000210E597B5E0>  memory location
      students.itemsize     #1

'''

import numpy as np

students = np.array([[[1, 3, 5], [1, 1, 1]],
                     [[4.5, 4, 5], [4.3, 4.4, 4.6]]], dtype=int)

print(students,"\n")                # [[[1 3 5]
                                    #   [1 1 1]]
                                    # [[4 4 5]
                                    #  [4 4 4]]] 
print(students.shape,"\n")          # (2, 2, 3)
print(students.nbytes,"\n")         # 48
print(students.ndim,"\n")           # 3
print(students.dtype,"\n")          # int32
print(students.size,"\n")           # 12
print(students.data,"\n")           # <memory at 0x00000265FF9A59A0>
print(students.itemsize,"\n")       # 4

'''
Arithmetic operators: elementwise application
'''

import numpy as np

x1 = np.array([[-1, 3]])
x2 = np.array([[1, 2]])
x3 = x1 + x2
x4 = x1 * x2
x5 = x1 - x2
print(x1)               # [[-1 3]]
print(x2)               # [[1 2]]
print(x3)               # [[0 5]]
print(x4)               # [[-1 6]]
print(x5)               # [[-2 1]]

# Careful with data types

x3 = np.power(10, 4, dtype = np.int8)
print(x3)               # 16 ((overflow int8 size))
x4 = np.power(10, 4, dtype = np.int32)
print(x4)               # 1000 ((correct value))

'''
Reshape vs Resize

Reshape using reshape. Total size must remain the same
'''

import numpy as np

print(np.arange(10))                        # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(10).reshape(2,5))           # [[0 1 2 3 4]
                                            #  [5 6 7 8 9]]
print(np.arange(10).reshape(2,7))           # ValueError: cannot reshape array of size 10 into shape (2,7)

print((np.resize(np.arange(10),(2,5))))     # [[0 1 2 3 4]
                                            #  [5 6 7 8 9]]
print((np.resize(np.arange(10),(2,7))))     # [[0 1 2 3 4 5 6]
                                            #  [7 8 9 0 1 2 3]]

'''
NEWAXIS
Adds a colum in the array  

COPY
Copy the array to other array 
'''

import numpy as np

d = np.arange(2, 5)             
print(np.arange(2, 5))          # [2 3 4]
print(d.shape)                  # (3,)
print(d[:, np.newaxis])         # [[2]
                                #  [3]
                                #  [4]]                             
print(d[:, np.newaxis].shape)   # (3, 1)

x = np.array([1, 4, 3])
y = x
z = np.copy(x)
x[1] = 2
print(x)            # [1 2 3]
print(y)            # [1 2 3]
print(z)            # [1 4 3]

'''
SORTING
Organizing a array using a specific parameter
'''

import numpy as np

dtype = [('name', 'S10'), ('grade', float), ('age', int)]
values = [('Joseanne', 5, 31), ('Hamed', 5, 32),
          ('Stefan', 5, 24)]
sorted_data = np.array(values, dtype = dtype)
print(np.sort(sorted_data, order = 'age'))      # [(b'Stefan', 5., 24)
                                                # (b'Joseanne', 5., 31)
                                                # (b'Hamed', 5., 32)]

# Remove the b
dtype = [('name', 'U8'), ('grade', float), ('age', int)]
values = [('Joseanne', 5, 31), ('Hamed', 5, 32),
          ('Stefan', 5, 24)]
sorted_data = np.array(values, dtype = dtype)
print(np.sort(sorted_data, order = 'age'))      # [('Stefan', 5., 24)
                                                # ('Joseanne', 5., 31)
                                                # ('Hamed', 5., 32)]

'''
Creating Zeros vectors and Matrices 
'''

import numpy as np

print(np.zeros((3)))            # [0. 0. 0.]
print(np.zeros((3, 4)))         # [[0. 0. 0. 0.]
                                #  [0. 0. 0. 0.]
                                #  [0. 0. 0. 0.]]
b = np.zeros((10, 6), dtype = int)
print(b)                        # [[0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]
                                #  [0 0 0 0 0 0]]
print(b.ndim, b.dtype, b.size)  # 2 int32 60

b = np.zeros(10)
b[8] = 1
print(b)                        # [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]

'''
Slicing arrays is almost the same as slicing lists,
except you can specify multiple dimensions

x[0,0]  	     # top-left element
x[0,-1] 	     # first row, last column
x[0,:]	         # first row (many entries)
x[:,0]	         # first column (many entries)

Notes:
- Zero-indexing
- Multi-dimensional indices are comma-separated (i.e., a tuple)
- Writing to a slice overwrites the original array
'''

import numpy as np

b = np.arange(10, 50)
print(b)                            # [10 11 12 13 14 15 16 17 18 19 20 21 22 23 
                                    #  24 25 26 27 28 29 30 31 32 33 34 35 36 37 
                                    #  38 39 40 41 42 43 44 45 46 47 48 49]
print(b.ndim, b.dtype, b.size)      # 1 int32 40

b = np.arange(50)
b = b[::-1]
b = b.reshape(5, 10)
print(b)                            # [[49 48 47 46 45 44 43 42 41 40]
                                    #  [39 38 37 36 35 34 33 32 31 30]
                                    #  [29 28 27 26 25 24 23 22 21 20]
                                    #  [19 18 17 16 15 14 13 12 11 10]
                                    #  [ 9  8  7  6  5  4  3  2  1  0]]
print(b[4, 1])                      # 8
print(b[3,:])                       # [19 18 17 16 15 14 13 12 11 10]
print(b[0,2:])                      # [47 46 45 44 43 42 41 40]
print(b[:1,1:])                     # [[48 47 46 45 44 43 42 41 40]]

'''
CONCATENATION, VSTACK, HSTACK

concatenate:    Join a sequence of arrays along an existing axis.
stack:          Join a sequence of arrays along an new axis.
block:          Assemble an nd-array from nested lists of blocks.
hstack:         Stack arrays in sequence horizontally (column wise).
dstack:         Stack arrays in sequence depth wise (along third axis).
column_stack:   Stack 1-D arrays as columns into a 2-D array.
vsplit:         Split an array into multiple sub-arrays vertically (row-wise).
'''

import numpy as np

b = np.arange(50)
b = b.reshape(5, 10)
c = np.ones((2, 10))
print(np.concatenate((b, c)))       # [[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]
                                    #  [10. 11. 12. 13. 14. 15. 16. 17. 18. 19.]
                                    #  [20. 21. 22. 23. 24. 25. 26. 27. 28. 29.]
                                    #  [30. 31. 32. 33. 34. 35. 36. 37. 38. 39.]
                                    #  [40. 41. 42. 43. 44. 45. 46. 47. 48. 49.]
                                    #  [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
                                    #  [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]]
a = np.arange(2, 6)
b = np.array([[3, 5], [4, 6]])
print(np.vstack(a))                 # [[2]
                                    #  [3]
                                    #  [4]
                                    #  [5]]
print(np.hstack(b))                 # [3 5 4 6]

'''
ONES, ZEROS_LIKE, ONES_LIKE, EYE, EMPTY, FULL

empty_like:             Return an empty array with shape and type of input.
ones:                   Return a new array setting values to one.
zeros:                  Return a new array setting values to zero.
full:                   Return a new array of given shape filled with value.
'''









