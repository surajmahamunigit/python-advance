######## Mathematical operators (+, *)  ##########

## dict1 + dict2 not allowed in python:

dict1={1:'A',2:'B',3:'C'}
dict2={100:'shiva',200:'ram'}

# dict3=dict1+dict2  --> TypeError


## dict1 * int is not allowed in Python:

#dict2=dict1*2  --> TypeError


########## Equality Operators (==, !=)###########

print(dict1 == dict2)  # False

print(dict1 != dict2)  # True


###########  Relational Operators (<, <=, >, >=) ###########

# Relational operators are not allowed in dict. if we tr to use it we will get TypeError

#print(dict1 > dict2)  --> TypeError
#print(dict1 >= dict2) --> TypeError


########## Membership Operators (in, not in) #########

print(10 in dict1)   # False
print(2 in dict1)  # True


