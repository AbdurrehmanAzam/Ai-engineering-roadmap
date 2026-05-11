a = "Hello"
print(id(a))
a = a + " World"
print(id(a))
# Strings are immutable so thats why their address changed

b = (1, 2, 3, 4)
print(id(b))
b = b + (5, 6, 7, 8)
print(id(b))
# The addresses of tuple changed meaning after editing new tuple have been formed
# This behaviour is called immutable

c = [1, 2, 3, 4]
print(id(c))
c.append(5)
print(id(c))

# this is example of list
