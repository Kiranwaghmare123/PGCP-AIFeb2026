class car:

    
    def __init__(self, name,speed):
        self.name = name
        self.speed = speed
        
    def accelerate(self, amount):
        self.speed += amount
        print(self.name, self.speed)
        
    def brake(self, amount):
        self.speed -= amount
        print(self.name, self.speed)

        
c1 = car("BMW", 120)
c1.accelerate(50)
c1.brake(20)

