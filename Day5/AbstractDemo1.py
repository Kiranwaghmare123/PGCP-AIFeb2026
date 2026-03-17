from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def display(self):
        pass
    
class Rectangle(Shape):
    
    def area(self):
        print("Area of rectangle")
        
    
    def display(self):
        print("Are ye Rectangle hai !")
        
r = Rectangle()
r.area()
r.display()