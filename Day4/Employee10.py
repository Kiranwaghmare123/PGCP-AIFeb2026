# constructor
class Employee:
    def __init__(self):
        self.name = "No id"
        self.sal = 0
        
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
    
    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.sal)
        

#emp = Employee()
#emp.display()
emp1 = Employee("Amit",50000)
emp1.display()



   


