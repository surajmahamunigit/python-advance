# Protected variable are only accessible from the same class of the child class

class Test:

    def __init__(self):
        self._a=10              # Protected variable

    def m1(self):
        print(self._a)

class SubTest(Test):

    def m2(self):
        print(self._a)


t=SubTest()
t.m1()   # 10
t.m2()     # 10

print(t._a)     # should be invalid but its not

#### In Python, modifiers are just for naming conventions, they are not built on basic level.
# we can access private and protected members from outside of the class.
# They are just there for good programming practice


