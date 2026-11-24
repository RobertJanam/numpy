import numpy as np

arr = [1, 2, 3]

vector = np.array(arr)

v = vector.view()

print(id(vector))
print(id(v))