import numpy as np

# append at the end of the array

arr = [1, 2, 3, 4]

vector = np.array(arr)

print(arr)

arr = np.append(arr, [5])
print(arr)

# appending another array at the end of a 1D array

arr1 = [6, 7, 8, 9, 10]

arr = np.append(arr, arr1)

print(arr)

# appending with a different array type

arr2 = [11.0, 12.0, 13.0, 14.0]

arr = np.append(arr, arr2)

print(arr)

# appending using list comprehension and numpy.concatenate

arr = np.array(arr, dtype=np.int64)

# print(arr)

values_to_append = [[15,16], [17, 18]]

combined = np.concatenate([arr] + values_to_append)

print(combined)