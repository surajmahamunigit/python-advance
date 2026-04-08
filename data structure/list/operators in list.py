## we are going to see multiple mathematical operators we can use with the list data structure

###########  Concatenation operator (+)  ##########

l1=[10,20,30]
l2=[40,50,60]

print(l1+l1)  # [10,20,30,40,50,60]

############# repetition operator (*) ######

print(l2*2)  # [40,50,60,40,50,60]
#print(l2*2.0)  # TypeError


######## Equality operator (==, !=)  #####################

print(11==l2)  # False

l3=["leroy", "raj", "kumar"]
l6=["Leroy","raj","kumar"]
l4=["raj","leroy","kumar"]
l5=["leroy","raj","kumar"]

print(l3==l4) # False
print(l3==l5) # True
print(l3==l6) # false --> elements should be in same order, same number, and case should be same


################### Comparison operator :

list1=[10,20,30]
list2=[10,20,6]
list3=['raj','leroy','kumar']
list4=["raj","leroy","Kumar"]

print(list1>list2) #True
print(list1<list2) # False

print(list4>list3) # False --> K < k


###################  Membership operators:

print(50 in list4) # False
print(10 in list1) # True



