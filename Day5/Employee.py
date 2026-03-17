class Employee:
    def __init__(self,name,sal):
        self.__name =  name
        self.__sal = sal   
    
    def display(self):
        print(self.__name)
        print(self.__sal)

emp = Employee("Rahul", 40000)

emp.display()
# print(emp.__name) : Error : direct access for private variables is not allowed