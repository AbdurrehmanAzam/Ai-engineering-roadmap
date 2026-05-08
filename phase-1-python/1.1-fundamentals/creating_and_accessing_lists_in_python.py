L = print([])
P = [2, 3, 4, 5, 6]
K = [2, "Hi", 2 + 4j, True]
print("P", P)

# Multi dimention lists
# 2D list
L1 = [4, 2, 5, 6, [2, 3], 6]
print("L1", L1[4][0])

# 3D list
L2 = [[[23, 34], [23, 56, 76]], [[23, 34], [23, 54, 23]]]
print("L2", L2[1][1][1])

# Converting string into list
L3 = list("My name is Abdurrehman")
print(L3)

L4 = list()
print(L4)

print(P[2])
print(P[2:4])
print(P[::-1])
print(P[0::2])
print(P[-4])
