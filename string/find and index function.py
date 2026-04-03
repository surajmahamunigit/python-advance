
s1= "Banana"

#    012345
#    ----->

print(s1.find('z')) # index -1 --> not in the string

print(s1.find('a')) # 1 --> left to right
print(s1.rfind('n')) # 4 --> first occurrence of letter in the string from right side and its index from right side

print(s1.find('a',3,5)) # index 3 to 4  --> 3
print(s1.rfind('b',1,5)) # index 1 to 4  --> -1 --> not there
print(s1.rfind('a',1,5)) # index 1 to 4  --> 3



#######################  index() function  ############

# index() function works just like find() except one thing. if index() doesnt find substring, it raises ValueError

email = input("Enter your email address: ")

try:
    index=email.index('@')   # if not present will raise Error
    print(index)
except ValueError:
    print("Invalid Email Address")


s1="ABCDEFG"

print()
print(s1.index('B',1,5)) # 1
#print(s1.index('B',4,7)) # ValueError

print(s1.rindex("D",1,6))  # 3




