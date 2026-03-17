class A:
    def m1(self):
        print("m1() : parent class method")
        
class B(A):
    def m2(self):
        print("m2() : child class method")
        
s = B()
s.m1()
s.m2()

s = A()
s.m1()
# s.m2() Error :AttributeError: 'A' object has no attribute 'm2'. Did you mean: 'm1'?