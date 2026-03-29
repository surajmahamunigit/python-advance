class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sayhello(self):
        print("Hello...")


class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def employeeinfo(self):
        print("Employee name: ", self.name)
        print("Emplyee age: ", self.age)
        print("Employee eno: ", self.eno)
        print("Employee salary: ", self.esal)

e=Employee("James",22,"1234",100)
e.sayhello()
e.employeeinfo()
