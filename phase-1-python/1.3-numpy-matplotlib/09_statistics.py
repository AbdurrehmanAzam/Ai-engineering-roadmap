import numpy as np

a = np.array([[1, 2, 3, 4, 5], [0, 7, 8, 9, 10]])
print(np.max(a, axis=1))
print(np.max(a, axis=0))
print(np.max(a))
print(np.min(a, axis=1))
print(np.min(a, axis=0))
print(np.min(a))

print(np.sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
