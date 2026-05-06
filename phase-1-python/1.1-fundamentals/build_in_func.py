# print() is used to display output to the console
print("Hello World!")

# input() pauses execution and prompts the user to enter text
name = input("Enter your name: ")
print(f"Your name is: {name}")

# type() returns the data type of a variable or value
a = 3
b = 4.5
c = "Abdurrehman"
print(f"a type is {type(a)},\nb type is {type(b)},\nc type is {type(c)}")

# int() converts a value into an integer data type
number = int(input("Enter the integer value: "))

# abs() returns the absolute (positive) value of a number
print(abs(-4.5))

# pow(base, exp) calculates the value of a base raised to a given power
print(pow(2, -3))

# min() and max() return the smallest and largest values from a list or iterable
print(f"minimum value is {min([1, 2, 3, 4, 5, 6, 7, 8])}")
print(f"maximum value is {max([1, 2, 3, 4, 5, 6, 7, 8])}")

# round() simplifies a number by rounding it to a specified number of decimal places
number2 = 22 / 7
print(round(number2, 7))

# divmod() returns a pair containing both the quotient and the remainder
print(divmod(2, 5))

# bin(), oct(), and hex() convert integers into binary, octal, and hexadecimal strings
print(bin(4))
print(oct(4))
print(hex(4))

# id() returns the unique memory address (identity) of an object
print(id(number))

# ord() returns the Unicode or ASCII integer value of a single character
print(ord("A"))

# len() returns the total length or number of items in an object, like a string or list
print(len("Abdurrehman Azam is my name"))

# sum() adds up all the numbers in an iterable (like a list) and returns the total
print(sum([1, 2, 3, 4, 5, 6, 7]))

# help() provides detailed documentation and information about any built-in function
print(help(divmod))
