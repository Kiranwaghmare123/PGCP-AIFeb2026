class A:
    def m1(self):
        print("m1() : parent class 1")
        
class B(A):
    def m2(self):
        print("m2() : child class 1")
        
class C(A):
    def m3(self):
        print("m3() : child class 2")

class D(B,C):
    def m4(self):
        print("m4() : child class level 2")  
        
d = D()
d.m1()
d.m2()
d.m3()
d.m4()     

d = C()
d.m1()
#d.m2()
d.m3()
#d.m4()    

d = B()
d.m1()
d.m2()
#d.m3()
#d.m4()   

d = A()
d.m1()
#d.m2()
#d.m3()
#d.m4()   