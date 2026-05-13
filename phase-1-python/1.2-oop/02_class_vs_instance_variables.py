class Employee:
    def __init__(self, name, roll_number, salary):
        self.name = name
        self.roll_number = roll_number
        self.salary = salary

    def raise_salary(self, salary_increased):
        self.amount = salary_increased
        self.salary = self.salary * salary_increased
        return self.salary


salary = float(input("Enter the salary : "))
employee_1 = Employee("Abdurrehman", 14, salary)
print(employee_1.name)
print(employee_1.roll_number)
print(employee_1.salary)
salary_increased = float(
    input("Enter the amount by which you want your employee salary to raise : ")
)
new_salary = employee_1.raise_salary(salary_increased)
print(f"The new salary of {employee_1.name} = {new_salary}")
