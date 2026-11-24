import numpy as np

arr = np.array([
    [-1, 2, 0, 4],
    [4, -0.5, 6, 0],
    [2.6, 0, 7, 8],
    [3, -7, 4, 2.0]
])

# slicing. [start:stop:step]
# "Python" as an example
# [1:4] - yth
# [:3] - Pyt
# [2:] - thon
# [::2] - Pto (start from 0, to the last index, skip 2 steps along the way)
# [-2:] - on (move 2 steps from the last index, count from that index to the last.)
# [::-1] - nohtyP (start from 0, moving along to the last index, -1, reverses the sequence. Therefore, start from last to first)
# [:] - Python (create a shallow copy)

arr1 = arr[:2, ::2]

print(arr1)

# (Row, column) index = 0
# (1, 3), (1, 2), (0, 1), (3, 0)

arr2 = arr[[1, 1, 0, 3], [3, 2, 1, 0]]

print(arr2)


