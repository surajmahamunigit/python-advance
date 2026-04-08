# comprehension concept is not applicable for tuple. if we try to use it, it will return 'generator' class object

t1=(x*x for x in range(1,6))
print(t1)  # generator object

# we can cast it to tuple

t2=tuple(x*x for x in range(1,6))
print(type(t2))  # <class 'tuple'>
print(t2)  # (1, 4, 9, 16, 25)


# we can also use list comprehension to create tuple

t3=tuple([x*2 for x in range(1,6)])
print(t3)   #  (2, 4, 6, 8, 10)