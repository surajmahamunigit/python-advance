list1=[10,20,30]

#append()
list1.append(40)  # always adds at the end of the list
list1.append(50)
print(list1)  # [10, 20, 30, 40, 50]

#insert()
list1.insert(1,9999)
list1.insert(1000, 60) # index value > len(l)
list1.insert(-1111, 0) # index value > len(l)
print("after insert():")
print(list1) # [0, 10, 9999, 20, 30, 40, 50, 60] --> elements added at start and end

#extend()
print()
list1=[10,20,30]
list2=[70,80]
list1.append(list2)  # append: [10, 20, 30, [70, 80]] --> len=4
print(list1)

list1=[10,20,30]
list2=[70,80]
list1.extend(list2)
print(list1)  ## [10, 20, 30, 70, 80] --> len=5
print()

#count()
print("given numbers count is :",list1.count(10))  # 1
print("given numbers count is :",list1.count(100)) # 0


#index()
print()

print("Index of number is",list1.index(10)) # index is: 0
#print("Index of number is:",list1.index(200))  #ValueError --> doesnt not present in the list

#