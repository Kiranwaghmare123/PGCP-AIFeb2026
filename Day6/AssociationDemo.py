class Student:
    def __init__(self,name):
        self.name = name
    
    
class Teacher:
    def __init__(self,name):
        self.name = name
    
    def teach(self, student):
        print(f"{self.name} teaches {student.name}")
        
s1 = Student("Ravi")
t1 = Teacher("Neha")

t1.teach(s1) # Association is created at s1
        
        
        
    