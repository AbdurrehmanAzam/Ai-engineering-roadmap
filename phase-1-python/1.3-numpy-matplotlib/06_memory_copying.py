import numpy as np

# Copying has an issue here

a = np.array([1, 2, 3])
b = a
b[:] = 5, 6, 7
print(a)
# Even though i changed the value of b the a changed
# To fix this issue we use .copy() func
a = np.array([1, 2, 3])
b = a.copy()
b[:] = 5, 6, 7
print(a)
# See it didnt change
