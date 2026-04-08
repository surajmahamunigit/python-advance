#
list1=[40, 100,10,20,30]
print("Before: ", list1)

list1.sort()
print("After: ", list1)

# output:
# Before:  [40, 100, 10, 20, 30]
# After:  [10, 20, 30, 40, 100]


#
list2=["raj","kumar","Anni"]
print("Before: ", list2)

list2.sort()
print(list2)

# output:
# Before:  ['raj', 'kumar', 'Anni']
# ['Anni', 'kumar', 'raj']


# reverse sorting
list3=[10,20,30,40,50]
print("Before: ", list3)

list3.sort(reverse=True)  # look carefully
print("After: ", list3)

# output:
# Before:  [10, 20, 30, 40, 50]
# After:  [50, 40, 30, 20, 10]


# heterogeneous objects
list4=["raj",10,"kumar","Anni"]
print("Before: ", list4)

# list4.sort()  --> can only sort homogeneous members
# print("After: ", list4)
# output: TypeError: '<' not supported between instances of 'int' and 'str'>


########### sorted()  #########
list5=[10,20,30,100,9,1]
print("Before: ", list5)

rev_list5 = sorted(list5)  # in-built functon in python, it returns sorted list
print("After: ", rev_list5)

# output:
# Before:  [10, 20, 30, 100, 9, 1]
# After:  [1, 9, 10, 20, 30, 100]
