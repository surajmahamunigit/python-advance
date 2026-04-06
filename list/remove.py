l=[1,1,2,2,2,2,3,4,5,6]
l.remove(2)  # will remove the first occurrence of the 2 if present in the list or will return ValueError
print(l)  # [1, 1, 2, 2, 2, 3, 4, 5, 6]

# write a program to remove all the occurrences of given number from the list

#user input
list1=[10,10,20,30,40,50,60]

#logic

x=int(input("Enter the number you want to remove from the list: "))

#check if the given element is present in list before trying to remove it
#if we dont check there is chance we will get ValueError

#do it to remove all the occurrences
while True:
    if x in list1:
        list1.remove(x)

    else:
        print("Please enter the valid number")
        break

print(list1)
# [20, 30, 40, 50, 60]
