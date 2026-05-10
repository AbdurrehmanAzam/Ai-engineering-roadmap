D1 = {"Name": "Abdurrehman", "Age": "21"}
D2 = {
    "Name": "Abdurrehman",
    "University": "USTB",
    "Marks": {"Urdu": 45, "English": 50, "Maths": 49},
}
# you cannot add or multiply dictonaries
# but you can apply loops on dictonaries
for i in D2:
    print(i)
# it will only print keys dictonary is all about keys to print values too we use this method
for i in D2:
    print(i, D2[i])

print("Urdu" in D2)
print("Urdu" in D2["Marks"])
print(45 in D2["Marks"].values())
