import numpy as np

# fill array with zeros
arr_zero = np.zeros((2, 3)) # 2 rows, 3 columns
print(arr_zero)

# fill array with ones
arr_one = np.ones((2, 3))
print(arr_one)

# fill array with specific values

arr_full = np.full((2, 3), 7) # filled with values of 7 
print(arr_full)

# fill array with random values
arr_random = np.random.rand(2, 3) # 2x3 random floats
print(arr_random)

# fill array with random values (int)
arr_random_int = np.random.randint(1, 10, size=(2, 3)) # range from 1 to 9, 2x3
print(arr_random_int)

# fill array with a range of values
arr_range = np.arange(0, 10, 2) # range of 0 to 10, skip 2
print(arr_range)

# fill array with a range of values evenly spaced
arr_linspace = np.linspace(0, 10, 5)
print(arr_linspace)

