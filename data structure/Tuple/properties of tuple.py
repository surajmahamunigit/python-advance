#
#
# insertion order is preserved
# duplicates are allowed
# heterogeneous objects are allowed
# indexing and slice is allowed
# immutable
# ()


t1=()
# t2=(10) --> not a tuple -> int type
# t3=10  --> not a tuple -> int type
t4=(10,)
t5=10,
t6=(10,20,30)
t7=10,20,30
t8=(10,20,30,)
t9=10,20,30,

# tuple are immutable
t1=(10,20,30,)
#t1(1)=999  --> TypeError

t4=eval(input("enter tuple:"))
print(t4)