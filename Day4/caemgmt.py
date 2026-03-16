class car:
    sp = 30
    
    def __init__(self, name,speed):
        self.name = name
        self.speed = speed
        
    def accelerate(self, amount):
        self.speed += amount
        print(self.name, self.speed)
        
    def brake(self, amount):
        self.speed -= amount
        print(self.name, self.speed)
        
    def speed(self):
        print("Speed=",car.sp)
        
c1 = car("BMW", 120)
c1.accelerate(50)
c1.brake(20)
c1.speed()
