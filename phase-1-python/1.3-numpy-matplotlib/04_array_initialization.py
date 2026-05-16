import numpy as np

b = np.array(
    [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
)

print(np.zeros((5, 4, 7), dtype="int8"))

print(np.full((4, 4), 77, dtype="float32"))
print(np.full_like(b, 2))
print(np.full(b.shape, 3))
print(np.random.rand(2, 2))
print(np.random.random_sample(b.shape))
print(np.random.randint(5, 11, size=(3, 3)))

print(np.identity(4, dtype="int8"))

c = np.array([["*", "*", "*"]])
r1 = np.repeat(c, 5, axis=0)
print(r1)
