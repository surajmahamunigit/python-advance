# single class inheriting properties from multiple classes

class A:
    def m1(self):
        print("Parent Method")

class B(A):
    def m2(self):
        print("Parent-Child method")

class C(B):
    def m3(self):
        print("Child class method")


c=C()
c.m1()  # multilevel
c.m2()  # multilevel
c.m3()
