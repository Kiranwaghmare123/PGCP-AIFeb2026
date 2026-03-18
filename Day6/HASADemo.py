class Engine:
    def __init__(self,engine_no,power):
       self.engine_no = engine_no
       self.power = power
       
    def start(self):
        print(f"Engine {self.engine_no} with capacity {self.power}")
        
class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine
        
    def start1(self):
        print(f"Brand name = {self.brand} with model = {self.model} and having engine= {self.engine}")
        self.engine.start()
        
    def display(self):
        print("Car details............")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Engine details : {self.engine}")
        print(f"Power : {self.engine.power}")
        
e1 = Engine("ABC2020221", 150)
c1 = Car("Honda","City",e1)

c1.start1()
c1.display()
        
        
        
        