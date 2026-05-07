# COMMON FUNCTIONS
# 1.len
sentence = "It is a good life we lead, brother. The best. May it never change us."
print(len(sentence))

# 2.max
print(max(sentence))

# 3.min
print(min(sentence))

# 4.1 sorted but ascending order
print(sorted(sentence))
# 4.2 sorted but descending order
print(sorted(sentence, reverse=True))

# STRING UNIQUE FUNCTIONS THAT ARE ONLY APPLICABLE ON STRING
# capatalize/title/upper/lower/swapcase
print(sentence.capitalize())

print(sentence.title())

print(sentence.upper())

print(sentence.lower())

print(sentence.swapcase())

# count
print(sentence.count("is"))

# find/index
print(sentence.find("b"))

print(sentence.index("n"))

# startswith/endswith
print(sentence.endswith("us."))

print(sentence.startswith("it"))

# format
print("My name is {} and I am {} years old".format("Abdurrehman", 21))
print("My name is {0} and I am {0} years old".format("Abdurrehman", 21))
print("My name is {age} and I am {name} years old".format(name="Abdurrehman", age=21))
print("My name is {} and I am {} years old".format(21, "Abdurrehman"))

# isalnum/ isalpha/ isdecimal/ isdigit/ isidentifier
print(sentence.isalnum())
print(sentence.isalpha())
print(sentence.isdecimal())
print(sentence.isdigit())
print(sentence.isidentifier())

# split
print(sentence.split("i"))
new_sentence = sentence.split("i")

# join
print("-".join(new_sentence))

# replace
print(sentence.replace("is", "?"))

# strip
print(sentence.strip())
