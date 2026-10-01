# NumPy is a library for the Python programming language,
# adding support for large, multi-dimensional arrays and matrices,
# along with a large collection of high-level mathematical functions to operate on these arrays.

# pipenv install numpy

# import numpy as np

# print(np.array([1, 2, 3])) - return a 1D array

# print(np.array([[1, 2, 3], [4, 5, 6]])) - return a 2D array

# print(np.array([[1, 2, 3], [4, 5, 6]])) - return a 3D array

# print(np.array([[1, 2, 3], [4, 5, 6]])) - return a 4D array

# print(np.array([[1, 2, 3], [4, 5, 6]])) - return a 5D array

# typeof(np.array([[1, 2, 3], [4, 5, 6]])) - return <class 'numpy.ndarray'>

# print(np.array([[1, 2, 3], [4, 5, 6]]).shape) - return (2, 3) - 2D array

# np.zeros((2, 3)) - return a 2D array of zeros (2 rows, 3 columns)
"""
[[0. 0. 0.]
 [0. 0. 0.]]
"""


# np.zeros((2, 3), dtype=int) - return a 2D array of zeros (2 rows, 3 columns) of type int
"""
[[0 0 0]
 [0 0 0]]
"""

# np.ones((2, 3), dtype=int) - return a 2D array of ones (2 rows, 3 columns) of type int
"""
[[1 1 1]
 [1 1 1]]
"""

# np.full((2, 3),5, dtype=int) - return a 2D array of ones (2 rows, 3 columns) of 5 rows
"""
[[5 5 5]
 [5 5 5]]
"""


# np.random.random((2, 3)) - return a 2D array of random numbers (2 rows, 3 columns)
"""
[[0.12345678 0.23456789 0.34567890]
 [0.45678901 0.56789012 0.67890123]]
"""

# array - np.random.random((2, 3), dtype=int) - return a 2D array of random numbers (2 rows, 3 columns) of type int
"""
[[0 0 0]
 [0 0 0]]
"""


# array[0,1] - return the value at the first row, second column
"""
0
"""

# array[0,:] - return the first row
"""
[0 0 0]
"""

# array[:,0] - return the first column
"""
[0
 0]
"""

# array[:,:] - return the entire array
"""
[[0 0 0]
 [0 0 0]]
"""

# array[0:2,0:2] - return the first 2 rows, first 2 columns
"""
[[0 0]
 [0 0]]
"""

# array > 0.5 - return the array where the value is greater than 0.5
"""
[[False False False]
 [False False False]]
"""

# np.sum(array) - return the sum of the array
"""
0
"""

# np.sum(array, axis=0) - return the sum of the array by the columns
"""
[0 0 0]
"""

# np.sum(array, axis=1) - return the sum of the array by the rows
"""
[0 0]
"""

# np.round(array) - return the array rounded to the nearest integer
"""
[[0 0 0]
 [0 0 0]]
"""

# np.round(array, decimals=2) - return the array rounded to 2 decimal places
"""
[[0.00 0.00 0.00]
 [0.00 0.00 0.00]]
"""

# first = np.array([1, 2, 3])
# second = np.array([4, 5, 6])

# print(first + second) - return the sum of the two arrays
"""
[5 7 9]
"""


# dimensions_inch = np.array([1, 2, 3])
# dimensions_cm = dimensions_inch * 2.54
# print(dimensions_cm) - return the dimensions in centimeters
"""
[2.54 5.08 7.62]
"""


# dimensions_inch = [1,2,3]
# dimensions_cm = [x* 2.54 for x in dimensions_inch]
"""
[2.54 5.08 7.62]
"""
