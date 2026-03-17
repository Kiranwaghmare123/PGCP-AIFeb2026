class A:
    def m1(self):
        print("m1() : parent class 1")
        
class B:
    def m2(self):
        print("m2() : parent class 2")
        
class C(A,B):
    def m3(self):
        print("m3() : child class")
c = C()
c.m1()
c.m2()
c.m3()
#-----
c = B()
#c.m1() 
c.m2()
#c.m3()
#-----
c = A()
c.m1()
#c.m2()
#c.m3()