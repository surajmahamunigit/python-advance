####### concatenation operator (+)  ######
t1=(10,20,30)
t2=(30,40,50)

list1=[100,200,300]

print(t1+t2)
#print(t1+10)
#print(t1+list1)

# o/p:
# (10, 20, 30, 30, 40, 50)
# TypeError
# TypeError


########## repetition operator (*) ############

t1=(10,20,30)
t2=(30,40,50)

print(t1 * 2)
print(t1 * 0)
print(t1 * -1)
print(t1 * 3)

# o/p:

# (10, 20, 30, 10, 20, 30) --> 2 times repeated
# ()  --> empty
# ()  --> empty
# (10, 20, 30, 10, 20, 30, 10, 20, 30) --> 3 times


########## Equality Operator (==, !=)####

t1=(10,20,30)
t2=(10,20,30)
t3=(10,777,999)

print(t1==t2)
print(t1!=t3)

# o/p:
# True
# True


######## Relational Operator (<,<=,>,>=)  ########

t1=(10,20,30)
t2=(10,20,30)
t3=(10,777,999)

print(t1<t2)
print(t1<=t2)
print(t1>t3)
print(t1>=t3)
print(t1==t3)

# o/p:
# False
# True
# False
# False
# False


######## Membership Operator (in, not in)  ####

t1=(10,20,30)

print(10 in t1)
print(1000 in t1)
print(1000 not in t1)

# o/p:
# True
# False
# True


