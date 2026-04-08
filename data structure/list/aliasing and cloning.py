########### Aliasing ##########
from list.sort import list2

list1=[10,20,30,1,33]

list1=list2

list1.append(999)

print("list1 and list2 point to same object: ", list1 is list2)
# output: list1 and list2 point to same object:  True


######### cloning  ###############

list1=[10,20,30,1,33]

list2=list1.copy()  # or we can do list2=list1[::]

list2.append(999)
print("list1 and list2 point to same object: ", list2 is list1)
# output: list1 and list2 point to same object:  False

