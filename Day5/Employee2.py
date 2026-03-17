class Employee:
    def __init__(self,name,sal):
        self.__name =  name
        self.__sal = sal   
        
   #Getter method : read data
    def get_sal(self):
        return self.__sal
    
    def set_sal(self, amount):
        if amount > 0:
            self.__sal  = amount
        else:
            print("Invalid salary !!!!")
    
    def display(self):
        print(self.__name)
        print(self.__sal)

emp = Employee("Rahul", 40000)
emp.display()
emp.set_sal(70000) #setter
#emp.display()
print("Updated sal = ",emp.get_sal()) #getter



