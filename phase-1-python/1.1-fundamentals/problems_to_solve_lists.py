# Problem 1
sentence = "Hello my name is abdurrehman"

sentence.split()

L = []

for i in sentence:

    L.append(i.capitalize())
print(" ".join(L))
# Problem 2
string = "abdurrehmanazam@gmail.com"
print(string[0:11])
# problem 3
title1 = [1, 1, 2, 2, 3, 3]
unique_title = list(set(title1))
print(unique_title)
