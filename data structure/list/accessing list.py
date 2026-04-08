#we can access elements of the list 2 different ways:

# 1.using the index of the list

l=[0,1,2,3,4,5,6,7,8,9,10]

i=0

while i<len(l):
    print(l[i])
    i=i+1

# 2. directly accessing element

for x in l:
    print(x)


########### Program 1  ###########

# write a program to print the even elements of the list

for x in l:
    if x%2==0:
        print(x)