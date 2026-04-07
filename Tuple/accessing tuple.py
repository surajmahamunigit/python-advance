## Accessing tuple elements

########## using index

t=(10,20,30,40)

print(t[0])
print(t[1])
print(t[-1])

# output:
# 10
# 20
# 40


####### using slicing operator

print(t[:])
print(t[::2])
print(t[2::])
print(t[::-1])

# output:
# (10, 20, 30, 40)
# (10, 30)
# (30, 40)
# (40, 30, 20, 10)