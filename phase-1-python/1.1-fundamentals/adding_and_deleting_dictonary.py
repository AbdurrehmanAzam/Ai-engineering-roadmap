D1 = {"Name": "Abdurrehman", "Age": "21"}
D2 = {
    "Name": "Abdurrehman",
    "University": "USTB",
    "Marks": {"Urdu": 45, "English": 50, "Maths": 49},
}
D1["Grade"] = "A+"
print(D1)
D2["Marks"]["DSA"] = 40
print(D2)
# Deletion
D3 = {}
del D3
del D1["Age"]
print(D1)
# TO empty a dictonary we use clear function
D1.clear()
print(D1)
