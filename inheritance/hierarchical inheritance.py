class A:
    def m1(self):
        print("Parent class method")

class B(A):
    def m2(self):
        print("Child Class 1 method")

class C(A):
    def m3(self):
        print("Child Class 2 method")

b=B()
b.m1() # hierarchy
b.m2()

c=C()
c.m1() # hierarchy
c.m3()
