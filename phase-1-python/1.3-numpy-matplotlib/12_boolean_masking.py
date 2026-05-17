import numpy as np

a = np.genfromtxt(r"D:\AI Engineering\Codes\Random number text.txt", delimiter=",")

print(a > 34)
print(a[a > 34])
# You can get index as a list in numpy
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(b[[0, 3, -1]])
b[[0, 3, -1]] = [45, 23, 19]
print(b[[0, 3, -1]])
print(a)
print(np.any(a > 34, axis=0))
print(np.all(a > 34, axis=0))
print(np.any(a > 34, axis=1))
print(~(a > 34) & (a < 100))
