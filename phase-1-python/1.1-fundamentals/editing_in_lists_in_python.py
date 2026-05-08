L = [10, 20, 30, 40, 50]
L1 = [4, 2, 5, 23]
L[0] = 100
L[4] = 500
L[3::-1] = 200, 300, 400, 500

# Addition
L.append(1000)
L.append([5, 3])
L.extend([2, 1, 2, 5, 6])
L.extend("Hi")
L.insert(2, "hello")

print(L)

# Deletion
del L1

del L[0]
print(L)
del L[-2:]
print(L)
L.remove([5, 3])
print(L)
L.pop()
print(L)
L.pop()
print(L)
L.pop()
print(L)
L.clear()
print(L)
