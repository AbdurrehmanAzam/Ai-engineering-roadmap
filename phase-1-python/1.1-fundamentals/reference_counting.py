a = "Abdurrehman"
b = a
c = b
print(id(a))
print(id(b))
print(id(a))

import sys

print(sys.getrefcount(a))

a = 2
b = a
c = b

print(id(a))
print(id(b))
print(id(a))

import sys

print(sys.getrefcount(a))
