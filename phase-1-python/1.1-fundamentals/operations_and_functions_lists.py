# Operations
L1 = [2, 1, 3, 5, 4]
L2 = [6, 7, 8, 9, 10]
print(L1 + L2)

print(L1 * 3, L2 * 2)

for i in L1:
    print(i)

# Membership
print(2, 3 in L1)

# FUNCTIONS
print(sorted(L1))
print(L1)
print(sorted(L1, reverse=True))
print(L1)
L1.sort()
print(L1)
L1.sort(reverse=True)
print(L1)
L1.sort()
print(L1.index(3))
