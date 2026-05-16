import numpy as np

a = np.full((5, 5), 1)
print(a)
b = np.full((3, 3), 0)
print(b)
b[1, 1] = 9
print(b)
a[1:4, 1:4] = b
print(a)
