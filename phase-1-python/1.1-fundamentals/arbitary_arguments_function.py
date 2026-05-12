def plus(*number):
    sum = 0
    for i in number:
        sum = sum + i
    return sum


print(plus(1, 1, 1, 1))
