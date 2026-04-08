# write a program to remove the duplicate elements in the list

#user input
list1=[10,20,10,20,30]

#output:
result=[]

for num in list1:
    if num not in result:
        result.append(num)

print(result)  # o/p: [10, 20, 30]