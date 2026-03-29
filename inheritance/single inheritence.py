class P:
    def m1(self):
        print("Parent Method")

class C(P):
    def m2(self):
        print("Child Method")

c=C()
c.m1()
c.m2()

# The concept of inheriting properties from one class to another class is single inheritance
