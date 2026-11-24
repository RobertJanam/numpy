# append values at the end of the N-dimensional array
import numpy as np

arr = np.arange(1, 11).reshape(2, 5) # reshape (r, c). from [1, 2, 3, 4] (2, 2) reshapes to [[1, 2], [3, 4]]

print(arr)

col = np.arange(11, 16).reshape(1, 5) # column to append

print(col)

new_arr_col = np.append(arr, col, axis=0) # axis=0. appends vertically as new rows to the bottom

print(new_arr_col)

# NOTE: axis=1 appends horizontally to the right as new columns. the number of rows must match

# append row wise
row = np.zeros((2, 1)).reshape(2, 1)

print(row)

row = row.astype(int) # convert from float to int

new_arr_row = np.append(arr, row, axis=1)

print(new_arr_row)