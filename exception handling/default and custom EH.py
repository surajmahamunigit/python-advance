# Default Exception Handling: Whenever the exception occurs,
# PVM will create the corresponding exception object and check for handling code.
# In Default Exception handling case its not available. so, Python interpreter terminates the program
# and prints the corresponding exception information to the console

class Test:

    print("Hello World")

    # print(10/0)          # Abnormal termination--> ZeroDivisionError: division by zero

    print("End of Test")   # This part will never execute


####### Custom Exception Handling ############

class Test:
    print("Hello World")

    try:
        print(10/0)
    except ZeroDivisionError:
        print("Not Possible: Division by zero")

    print("End of Test")