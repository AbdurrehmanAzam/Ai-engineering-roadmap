D = {}
D1 = {"Name": "Abdurrehman", "Age": "21"}
print("D : ", D)
print("D1 : ", D1, type(D1))
D2 = {(1, 2, 3, 4, 5), "Abdurrehman"}
print(D2)

# Dictonary Keys should be unique
D3 = {"Name": "Abdullah", "Name": "Abdurrehman"}  # noqa: F601
print(D3)

# 2D dictonaries
D4 = {
    "Name": "Abdurrehman",
    "University": "USTB",
    "Marks": {"Urdu": 45, "English": 50, "Maths": 49},
}
print(D4)
