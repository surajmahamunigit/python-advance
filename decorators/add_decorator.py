
def decor_add_income(func):
    def inner(income1,income2):
        if income1<=0 or income2<=0 :
            print("income cannot be less than 0")
        else:
            print("#"*30)
            total_income=func(income1,income2)
            print(f"Total income is : {total_income}")
            print("#"*30)
    return inner

@decor_add_income
def add_income(income1,income2):
    """Adds two incomes"""

    return income1+income2

# Calling add_income() function
add_income(10200,11200)