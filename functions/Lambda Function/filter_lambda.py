# Case 1: find the sum of first 100 numbers
from functools import *

result=reduce(lambda num1,num2:num1+num2, range(1,101))
print(result)

