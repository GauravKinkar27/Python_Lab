class Employee:
    company = "ABC Corp"
    employee_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

print(f"Initial employee count: {Employee.employee_count}")
e1 = Employee("John", 50000)
e2 = Employee("Jane", 60000)
e1.display()
e2.display()
print(f"Total employees: {Employee.employee_count}")
print(f"Class variable accessed via class: {Employee.company}")
