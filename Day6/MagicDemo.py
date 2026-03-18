class Test:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
        
    def __str__(self):
        return f"Employeename: {self.name},Salary: {self.sal}"
    
    def __len__(self):
        return len(self.name)
    
    def __add__(self, other):
        return self.sal + other.sal

t1 = Test("Rahul",40000)
t2 = Test("Laxman",50000)
print(t1)
print(len(t1))
print(t1 + t2)
