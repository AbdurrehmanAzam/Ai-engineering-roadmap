class student:
    pass


student_1 = student()
student_2 = student()

student_1.name = "Abdurrehman"
student_1.email = "abdurrehmanazam300@gmail.com"
student_1.roll_number = 14

student_2.name = "Test"
student_2.email = "test@gmail.com"
student_2.roll_number = 20

print(student_1.name)
print(student_2.name)


# Entering manually the data is hassle so we use another method called __init__ OR contstructor
# Making another class with __init__ Method to automatically pass the values
class employee:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number


employee_1 = employee("Abdurrehman", 14)
print(employee_1.name)
print(employee_1.roll_number)

# Look below method is so much easier you can make as many as instances
# but you only have to pass the values through constructor
