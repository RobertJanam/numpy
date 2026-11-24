import numpy as np

arr = [1, 2, 3]

vector = np.array(arr)

v = vector.copy()

print(id(vector))
print(id(v))