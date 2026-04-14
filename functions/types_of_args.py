def positional_args(first_num=0,second_num=0):
    """In this function, order and number of args matter a lot
    Args: first_arg, second_arg
    Returns:"""

    print(f"first arg is {first_num} and second arg is {second_num}")


def variable_length_arg(*arguments):
    """This function takes variable number of arguments
    Args: variable length arguments
    Returns:sum of all arguments"""


    print(type(arguments))
    print(arguments)

    sum=0
    for arg in arguments:
        if type(arg)==tuple or type(arg)==list:
            break
        sum=sum+arg

    return sum


# Positional Arguments:
positional_args(10,20)
print()

# Keyword Argument:
positional_args(10,20)
positional_args(first_num=10,second_num=20)
positional_args(second_num=20,first_num=10)
positional_args(10,second_num=20)
#positional_args(first_num=10,20) --> SyntaxError

print()

# Default Arguments:
positional_args()
print()

# Variable length argument
print(variable_length_arg())
print()
print(variable_length_arg(10,20))
print()

print(variable_length_arg((10,20,30),(40,50,60)))
print()
print(variable_length_arg([10,20,30],[40,50,60]))



