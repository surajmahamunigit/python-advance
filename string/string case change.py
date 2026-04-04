#there are multiple methods

s1="Apple is Software COmpany"

#upper()
print("upper(): ", s1.upper())

#lower()
print("lower(): ",s1.lower())

#swapcase()
print("swapcase(): ",s1.swapcase())

#title()
print("title(): ",s1.title())

#capitalize()
print("capitalize(): ",s1.capitalize())

#output:
# upper():  APPLE IS SOFTWARE COMPANY
# lower():  apple is software company
# swapcase():  aPPLE IS sOFTWARE coMPANY
# title():  Apple Is Software Company
# capitalize():  Apple is software company


##################################################################

#write a program to compare two string s1 and s2 are equal or not
print()


s1="Apple"
s2="apple"

if s1==s2:
    print("Both string are same")
else:
    print("Both string are different")


# we can make s1 and s2 either uppercase or lowercase if case doesnt matter in comparison


###################################################################

#write a program to validate the given username and password is valid or not.
#username is not case sensitive

username=input("Enter the username: ")
password=input("Enter the password: ")

#username is changed to all lowercase
if username.lower()=="admin" and password=="1234":
    print("login successful")

else:
    print("login failed. Try again")


##########################################################################

#write a program to convert first and last character of the string into uppercase

str1=input("Enter a string: ")


output = str1[0].upper() + str1[1:len(str1)-1].lower() + str1[len(str1)-1].upper()
print("output string is: ",output)