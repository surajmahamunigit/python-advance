# Pre-defined Exceptions

# print(int("ten"))  -->  Pre-defined Exception --> ValueError: invalid literal for int()

# User-defined/Programmer/Custom Exception
# defined by programmers to raise custom exception.

class User:

    def validate(self,age):
        if 18 <= age < 110:
            print("You are old enough")
        else:
            raise InvalidAge("Not eligible")

class InvalidAge(Exception):

    def __init__(self,msg):
        self.msg=msg

u=User()
u.validate(112)  # User-defined exception --> InvalidAge: Not eligible
