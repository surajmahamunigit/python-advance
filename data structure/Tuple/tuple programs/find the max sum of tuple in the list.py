# write a program to find the tuple with max sum inside the list

#user input
list1=[(1,2),(3,4),(5,6)]

#core logic
max_sum = 0
max_tuple = list1[0]

#traverse the list and find the sum of each tuple
for t in list1:
    if sum(t)>max_sum:
        max_sum=sum(t)
        max_tuple=t

print("max sum of tuple {} is {}".format(max_tuple,max_sum))



