# Create
S1 = set()
print(type(S1))
S1 = {1, 1, 1, 2, 2, 2, 3, 3, 3}
S2 = {1, "Hello", 4 + 5j}
print("S1", S1)
print("S2", S2)

# Access items
# you cannot access items in sets

# You can add items in sets
S1.add(34.23)
print(S1)

# Deletion
# you cannot delete the spefic item on specefic index but you can delete whole set
del S2
S2 = {6, 2, 12, 5, 56}
S1.remove(3)
print(S1)

S1.pop()
print(S1)
# set operations
for i in S1:
    print(S1)

print(2 in S1)

# functions
print(len(S1))
print(min(S1))
print(max(S1))
print(sum(S1))
print(sorted(S1))
print(sorted(S1, reverse=True))

print(S1.union(S2))
print(S1.intersection(S2))
print(S1.difference(S2))
print(S2.difference(S1))
print(S1.symmetric_difference(S2))
print(S2.symmetric_difference(S1))
print(S1.isdisjoint(S2))
print(S1.issubset(S2))
print(S1.issuperset)
