#write a program to find second-largest number without using max or sorted

#user input
list1=[100,10,20,30,90]

#core logic
largest=list1[0]
second=None

i=1

while i<len(list1):
    if list1[i]>largest:
        second=largest
        largest=list1[i]


    elif list1[i]<largest and (second==None or list1[i]>second):
        second=list1[i]

    i=i+1

print("Second largest number: ",second)

