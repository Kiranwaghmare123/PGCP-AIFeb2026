class A:
    def m1(self):
        print("m1() : parent class 1")
        
class B(A):
    def m2(self):
        print("m2() : parent class 2")
        
class C(B):
    def m3(self):
        print("m3() : child class")

c1 = C()
c1.m1()
c1.m2()
c1.m3()
#------
c1 = B()
c1.m1()
c1.m2()
#c1.m3() Error
#------
c1 = A()
c1.m1()
#c1.m2()
#c1.m3()