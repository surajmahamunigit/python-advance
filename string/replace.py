#

#replace(old_string,new_string)

s1="ABABAB"
print(s1.replace("A","B")) #BBBBBB

s2='This is programming language'
print(s2.replace(" ","")) #Thisisprogramminglanguage

#we can use count() function to count number of spaces
print("Number of spaces in string: ",s2.count(" "))  # 3

#or we can use replace

print("Number of spaces in string: ",( len(s2) - len( s2.replace(" ","") )))  # 3

# replace() function always creates new string object

