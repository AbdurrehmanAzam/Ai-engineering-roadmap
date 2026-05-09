T2 = (1, 2, 3, 4, 5, 6)
T4 = (8, 23, 1, 54, 123, 12, 3)
# Editing
# You cannot edit tuples because tuples are immutable
# You cannot also do deletion in tuples but you can delete whole tuple
# you can perform certian operations on it
print(T2 * 3)
print(T2 + T4)
for i in T2:
    print(i)

# functions
print(len(T2))
print(max(T4))
print(min(T4))
print(sum(T4))
print(sorted(T4))
print(sorted(T4, reverse=True))
