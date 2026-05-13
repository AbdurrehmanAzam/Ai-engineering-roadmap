class Student:
    def __init__(self, sub1_marks, sub2_marks, sub3_marks):
        self.name = input("Enter your name : ")
        self.sub1_marks = sub1_marks
        self.sub2_marks = sub2_marks
        self.sub3_marks = sub3_marks

    def avg(self):
        average = float(self.sub1_marks + self.sub2_marks + self.sub3_marks) / 3
        return average


marks = []

for i in range(1, 4):

    score = int(input(f"Enter the marks for subject {i} : "))
    marks.append(score)


s1 = Student(marks[0], marks[1], marks[2])
print(f"Student '{s1.name}' your average is = {s1.avg()}")
