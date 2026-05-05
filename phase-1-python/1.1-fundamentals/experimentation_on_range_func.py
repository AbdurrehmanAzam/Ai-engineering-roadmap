i = 1
# # function range
while i in range(1, 11):
    print(f"{i}")
    i += 1

lastDigit = 40

i = 1
while i in range(lastDigit):
    print(f"{i}")
    i += 1

# skipping numbers

i = 2
while i in range(2, 21, 2):
    print(f"{i}")
    i += 2

# negative counting in range
for i in range(20, 1, -2):
    print(f"{i}")
