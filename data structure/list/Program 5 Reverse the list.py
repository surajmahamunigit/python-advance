#write a program to reverse the list. dont use reverse and slice

#user input
list1=[10,20,30,40]

#core logic
list2=[]
str1_len=len(list1) #4
index=str1_len-1

while index >= 0:
    list2.append(list1[index])
    index=index-1

print(list2)  # o/p: [40, 30, 20, 10]

