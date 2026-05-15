class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary


class Engineer(Employee):
    def __init__(self, role, department, salary, name, age):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)

    def show_details(self):
        print(
            f"Employee is Engineer\nEmployee name is {self.name}\nEmployee age is {self.age}\nEmployee role is {self.role}\nEmployee department is {self.department}\nEmployee salary is {self.salary}\n"
        )


eng1 = Engineer("Manager", "Software", "1000000", "Abdurrehman", "21")
eng1.show_details()
