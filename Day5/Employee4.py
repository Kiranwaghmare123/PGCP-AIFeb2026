class Employee:
    def __init__(self,name,sal):
        self.__name =  name
        self.__sal = sal   
        
    def calsal(self):
        bonus = self.__sal * 0.10
        total = self.__sal + bonus
        print("Total salary =",total)
    
    def display(self):
        print(self.__name)
        print(self.__sal)

emp = Employee("Rahul", 40000)
#emp.display()
emp.calsal()

