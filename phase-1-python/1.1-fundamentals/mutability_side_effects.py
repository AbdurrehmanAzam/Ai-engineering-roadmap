# If you assign one list to another variable, they point to the same memory address (Aliasing)
a = [1, 2, 3, 4, 5]
b = a
b.append(6)
print(a)
# Output will be [1, 2, 3, 4, 5, 6].
# Modifying 'b' also modifies 'a' because they share the same memory location.

# You can avoid this by cloning (copying) the list using slicing [:]
a = [1, 2, 3, 4, 5]
b = a[:]

print(id(a))
print(id(b))
# The addresses are now different.
# By cloning, 'b' is a brand new list in memory, so it won't affect your initial list.

b.append(6)
print(a)
# Output will be [1, 2, 3, 4, 5]. The original list remains safe.
