############## packing  ###########

a=10
b=20
c=30
d=40

t=(a,b,c,d)  # or t=a,b,c,d
print(t)  # o/p: (10, 20, 30, 40)


############# unpacking  #########

t1=(100,200,300,800)

a,b,c,d=t1
print(a,b,c,d)  # o/p: 100 200 300 800

# or
a,*b=t1
print(a,b)  #  o/p: 100 [200, 300, 800]  --> a=100, b=[200,300,800] (in list format)


a,b,c,d,e=t1  # ValueError: not enough values to unpack