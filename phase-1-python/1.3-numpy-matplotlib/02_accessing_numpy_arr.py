import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a)
print(a.shape)

# Get a specific element [rows , coloumn]
print(a[1, 2])

# Get a specific row
print(a[1, :])

# Get a specific coloumn
print(a[:, 2])

# Getting specific coloumns 2 to 4 coloum [startindex : endindex : stepsize]
print(a[:, 1:4])

# 3d array
b = np.array(
    [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
)
print(b[1, 1, 1])
print(b[:, :, 1:4])
