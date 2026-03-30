from inheritance.MRO import B


class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
b3=Book(300)

print("Total no of pages: ",b1+b2)

# b1+b2+b3 not possible

############  Magic Methods #########

# +  --> __add()__
# - --> __sum()__
# * --> __mul()__
# / --> __div()__
# //  --> _floordiv()__
# % --> __mod()__
# ** --> __pow()__


######  * operator overloading #######3

class Employee:
    def __init__(self,name,salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def __mul__(self,other):
        return self.salary_per_day*other.days


class TimeSheet:
    def __init__(self,name,days):
        self.name = name
        self.days = days


e=Employee("Raj", 500)
t=TimeSheet("Raj",50)

print("Total earning: ", e*t)

## we wrote __mul__() method in Employee class because in print we wrote e*t not t*e.
## t*e will give error with this code. we need to write __mul__() method in TimeSheet class to make it work
