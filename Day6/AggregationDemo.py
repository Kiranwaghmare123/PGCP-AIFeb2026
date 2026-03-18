class Employee:
    def __init__(self, name):
        self.name = name
        
class Department:
    def __init__(self, dname):
        self.dname = dname
        self.employees = []
        
    def add_emp(self, employee):
        self.employees.append(employee)
        
    def display(self):
        print(f"Department= {self.dname}")
        for emp in self.employees:
            print(emp.name)
              
e1 = Employee("Amit")
e2 = Employee("Sara")
    
d1 = Department("Education")
d1.add_emp(e1)
d1.add_emp(e2)

d1.display()
    