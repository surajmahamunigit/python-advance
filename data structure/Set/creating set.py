# there are multiple ay we can create the set

s1=set()
print(s1)  # empty set

s2={1,2,3}
print(type(s2))  #  <class 'set'>
print(s2)        # {1,2,3}

list1=[1,2,3,4]
s3=set(list1)
print(s3)     # {1,2,3,4}

s4=set(range(10,101,10))
print(s4)                  # {100, 70, 40, 10, 80, 50, 20, 90, 60, 30}


