import numpy as np

x = np.array([1, 2])

print(x.dtype)

y = np.array([1.0, 2.0])

print(y.dtype)

z = np.array([1, 2], dtype=np.int64)
print(z.dtype)

# Math operations

arr1 = np.array([[4, 7], [2, 6]], dtype=np.float64)
arr2 = np.array([[3, 6], [2, 8]], dtype=np.float64)

print(np.add(arr1, arr2))
print(np.sum(arr1))
print(np.sqrt(arr1))
print(arr1.T) # transpose. changing the order of the array