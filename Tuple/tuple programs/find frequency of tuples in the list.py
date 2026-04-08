# write a program to find the tuple frequency

#user input
list1=[(1,2),(3,4),(5,6),(1,2)]

#core logic
d={}
count=0

#traverse the list
for t in list1:
    d[t]=d.get(t,0) + 1

print(d)