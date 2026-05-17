import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# Reshaping numpy array
b = a.reshape((2, 5))
print(b)

# Vertically stacking arrays
v1 = np.array([5, 4, 12, 67, 34])
v2 = np.array([3, 2, 45, 67, 2])
# For vertical stacking arrays
print(np.vstack([v1, v2, v2, v1]))
# For horisental stacking arrays
print(np.hstack([v1, v2, v2, v1]))
