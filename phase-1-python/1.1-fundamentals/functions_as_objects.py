def square(number):
    return number**2


print(square(3))

x = square
print(x(3))

del square

print(x(3))
# Even though the orignal function is deleted the x function works
# Because here x is used as object

L = [1, 2, 3, x]
print(L[-1](3))

L = [1, 2, 3, 4, x(5)]
print(L)
