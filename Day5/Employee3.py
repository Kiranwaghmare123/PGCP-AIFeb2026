
#@property ans @setter
class Employee:
    def __init__(self,name,sal):
        self.__name =  name
        self.__sal = sal   
        
    @property
    def salary(self):
        return self.__sal
    
    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__sal  = amount
        else:
            print("Invalid salary !!!!")
    
    def display(self):
        print(self.__name)
        print(self.__sal)

emp = Employee("Rahul", 40000)
emp.display()
print("Salary =",emp.salary)

emp.salary = 55000
print("Updated Salary =",emp.salary)





