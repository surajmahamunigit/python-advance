class Person:
    def __init__(self,name,age):
        print("Parent constructor called..")
        self.name=name
        self.age=age

    def display(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)

class Employee(Person):

    def __init__(self,name,age,eno,pay):
        super().__init__(name,age)
        self.eno=eno
        self.pay=pay

    def display(self):
        super().display()
        print("Employee no: ",self.eno)
        print("Employee pay: ",self.pay)


e=Employee("Raj",32,101,10000)
e.display()