class student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number


s1 = student("Abdurrehman", 14)
print(s1.name, s1.roll_number)
del s1.name
print(s1.roll_number)
print(s1.name)
