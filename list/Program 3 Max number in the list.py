# write a program to find the largest number present in the list

#user input:
list1=[100,300,2,900]

#core logic:
max_num=list1[0]

#traverse the list
for num in list1:
    if num>max_num:
        max_num=num

print(max_num)  # o/p: 900



