# Call by object reference
a = 4
print(hex(id(a)))
print(hex(id(4)))
# Point proved because both 'a' and 4 have the same memory address.

# Aliasing
b = a
c = b
print(hex(id(b)))
print(hex(id(c)))
# They all have the same memory location because a, b, and c point to the same address.

del a
print(hex(id(c)))
print(hex(id(b)))
# Even if you delete the original variable 'a', the labels 'b' and 'c'
# still point to the original memory address.

a = 7
b = a
print(hex(id(a)))
print(hex(id(b)))

a = 19
print(hex(id(a)))
print(hex(id(b)))
# When a new value is assigned to 'a', its memory address changes.
# 'b' continues to point to the previous location.
