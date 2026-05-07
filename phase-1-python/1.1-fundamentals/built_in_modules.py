import math
import random
import time
import os

number = list(range(1, 11))

print(help("modules"))

print(math.log(100))
print(math.factorial(500))
print(math.pi)
print(math.e)

print(random.randint(1, 100))
random.shuffle(number)
print(number)
print(random)
print(time.time())
print(time.ctime())
print("Hello")
time.sleep(10)
print("World")

print(os.getcwd())
print(os.listdir())
