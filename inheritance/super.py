class P:

    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        print("Paren Class constructor")

    def display(self):
        print("Calling Parent class display: ",self.name,self.age,self.height,self.weight)

class C(P):

    def __init__(self,name,age,height,weight,rollno,marks):
        super().__init__(name,age,height,weight)
        self.rollno=rollno
        self.marks=marks

        P.display(self)  ## Another way of calling Parent class method.
                         ## Useful when working with multiple parent classes


    def display(self):
        super().display()
        print(self.rollno,self.marks)

c=C("Raj",22,6.3,190,101,99)
c.display()