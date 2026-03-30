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