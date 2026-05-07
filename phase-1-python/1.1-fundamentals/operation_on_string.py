# string concatenation(joining two strings together)
first_name = "Muhammad Abdurrehman "
last_name = "Azam\n"
full_name = first_name + last_name
print(f"My full name is : {full_name}", end="")

# string multiplication
print(full_name * 2, end="")

# Relational operators
print("Write 2 words same")
first_word = input("Enter your first word : ")
second_word = input("Now enter second word : ")
if first_word == second_word:
    print("Both words are same")
else:
    print("Both words are not same")

# Logical operators
print("" and "first_name", end="")
print("hi" and "hello ", end="")
print("" or "hi")
print("" or "")
print("hi" or "hi")
print(not "hello")
print(not "")

# Loops in string
for i in first_name[::-1]:
    print(i)

# Member operators
print("h" in first_name)
print("rreh" in first_name)
print("hehe" in last_name)
print("coke" in full_name)
