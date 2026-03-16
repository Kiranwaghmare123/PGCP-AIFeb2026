#Adding constructor and method for display the values
class Employee:
    #self : referes to current object
    def __init__(self, emp_id, emp_name, emp_salary): # initialize object data
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
     
        
    def show(self): # instance method
       print("Empl Id:",self.emp_id)
       print("Empl Name:",self.emp_name)
       print("Empl Salary:",self.emp_salary)
    
emp1 = Employee(111,"Ram", 10000)
emp1.show()
print()
emp2 = Employee(112,"Ravan", 1000)
emp2.show()


