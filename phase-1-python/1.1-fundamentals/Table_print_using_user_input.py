number = int(input("Enter the number of which you want to get table of : "))

i = 1

while i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
    i += 1

print("End of table")
