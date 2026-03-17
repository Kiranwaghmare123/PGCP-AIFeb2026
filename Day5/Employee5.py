class Employee:
    def __init__(self,name,sal, password):
        self.__name =  name
        self.__sal = sal   
        self.__password = password
        
    def login(self, password):
        if password == self.__password:
            print("Accesss granted")
        else:
            print("Access denied")
            
    def calsal(self):
        bonus = self.__sal * 0.10
        total = self.__sal + bonus
        print("Total salary =",total)
    
    def display(self):
        print(self.__name)
        print(self.__sal)

emp = Employee("Rahul", 40000,"emp123")
#emp.display()
emp.calsal()
emp.login("emp123") #Valid
emp.login("emp111") #Invalid

