import numpy as np

a = np.genfromtxt(r"D:\AI Engineering\Codes\Random number text.txt", delimiter=",")
a = a.astype("int8")
print(a)
