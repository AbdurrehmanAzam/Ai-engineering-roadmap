# Strings are immutable — you can't change them in-place
word = "hello"
try:
    word[0] = "H"
except TypeError as e:
    print("TypeError:", e)
print("String unchanged:", word)
