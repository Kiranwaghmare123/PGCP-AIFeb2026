class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print(f"{self.brand} {self.model} is starting.......")
        
    def stop(self):
        print(f"{self.brand} {self.model} is stopping.......")
        
class Car(Vehicle):
    def __init__(self,brand, model, fuel_type):
        super().__init__(brand, model) #Inheriting parent class variables
        self.fuel_type = fuel_type
        
    def display(self):
        print("Car Class Informations.....")
        print(f"Brand   :{self.brand}")
        print(f"Model   :{self.model}")
        print(f"Fuel type   :{self.fuel_type}")
        
class Bike(Vehicle):
    def __init__(self,brand, model, cc):
        super().__init__(brand, model) #Inheriting parent class variables
        self.cc = cc
    
    def display(self):
        print("Bike Class Informations.....")
        print(f"Brand   :{self.brand}")
        print(f"Model   :{self.model}")
        print(f"Capacity   :{self.cc}")
        
c1 = Car("Hyundai","Creta","Electric")
b1 = Bike("Royal Enfield", "Classic", 350)

c1.start()
c1.display()
c1.stop()

print()
b1.start()
b1.display()
b1.stop()