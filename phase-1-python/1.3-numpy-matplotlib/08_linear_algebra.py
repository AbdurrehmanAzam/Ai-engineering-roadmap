import numpy as np

# Multipling matrixes
a = np.full((2, 4), 4)
print(a)
b = np.full((4, 1), 7)
print(b)

c = np.matmul(a, b)
print(c)

# Finding the determinant
d = np.identity(5)
print(np.linalg.det(d))
