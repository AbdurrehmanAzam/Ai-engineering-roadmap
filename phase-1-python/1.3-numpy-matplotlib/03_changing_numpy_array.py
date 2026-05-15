import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a[1, 2])
# I want to change that 8 so
a[1, 2] = 30
print(a)
# Changing whole coloumn
a[:, 2] = 10, 20
print(a)

# 3d array
b = np.array(
    [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
)
b[1, 1, 1] = 1001
print(b)
b[:, :, 1:4] = [[[20, 30, 40], [70, 80, 90]], [[120, 130, 140], [170, 180, 190]]]
print(b)
