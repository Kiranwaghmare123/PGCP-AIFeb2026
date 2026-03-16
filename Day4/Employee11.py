class Employee:
    Company = "IBM"
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
        
    def display(self):
        print(self.name, self.sal,Employee.Company)
        
e1 = Employee("Ravi",50000)
e2 = Employee("Rachana",60000)
e1.display()
e2.display()