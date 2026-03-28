# inheriting properties from multiple class into one class

class A:
    def m1(self):
        print("Prent 1 method")

class B:
    def m2(self):
        print("Prent 2 method")

class C(A,B):
    def m3(self):
        print("Child method")

c=C()
c.m1() # multiple
c.m2() # multiple
c.m3()