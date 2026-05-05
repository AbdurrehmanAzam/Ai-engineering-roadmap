import random

number = random.randint(1, 100)
userinput = int(input("Guess the number between 1 and 100 : "))
i = 0
while userinput != number:
    if userinput < number:
        userinput = int(input("Guess higher : "))
        i += 1
    else:
        userinput = int(input("Guess lower  : "))
        i += 1

print(f"You entered the correct number! It took you {i} attempts.")
