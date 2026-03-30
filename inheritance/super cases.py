class A:

    a=10

    def __init__(self):
        self.b=20
        print("Parent Class constructor")

    def m1(self):
        print("Parent Class static method")

    @classmethod
    def m2(cls):
        print("Parent Class class method")

    @staticmethod
    def m3():
        print("Parent Class static method")

class B(A):

    def __init__(self):

        # Case 2 applies
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


    def display(self):

        # Case 1 we can access static variable but not the instance variable using super.# super().
        # super().b --> Invalid
        print(super().a)  # static variable
        print(self.b)  # but we can do it using self

        # Case 2 we can access constructor, instance method, class and static method
        #        of Parent class from Child classes Constructor and instance method
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


    # Case 3 From child classes class-method we:
    # can access class and static method of Parents class using super()
    # cant access instance method using super()
    @classmethod
    def m4(cls):
        super().m2()
        super().m3()

        # super().m1()  --> Invalid
        super(B,cls).__init__(cls)
        super(B,cls).m1(cls)


    #Case 4: From static method child class, you cant directly call Parent class
    # class-method and static method so we can,

    @staticmethod
    def m5():
        super(B,B).m2()  # calling Parent class class-method
        super(B,B).m3()  # calling parent class static method


