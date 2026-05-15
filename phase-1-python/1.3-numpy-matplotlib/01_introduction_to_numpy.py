import numpy as np

a = np.array([1.9, 2, 3, 4, 5], dtype="int8")
print(a)

b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype="int8")
print(b)

# Get dimenstion .ndim
print(a.ndim)
print(b.ndim)

# Get rows and coloumn .shape
print(a.shape)
print(b.shape)

# Get type of numpy .dtype
print(a.dtype)
print(b.dtype)

# Get size of single element .itemsize
print(a.itemsize)
print(b.itemsize)

# Get total size of numpy array
print(a.itemsize * a.size)  # Size of single item x Number of all element in numpy array
print(b.itemsize * b.size)

print(a.nbytes)  # Shortcut for total size of array
print(b.nbytes)
