### len()

t1=(10,20,30)
print(len(t1))  # 3

### count()

print(t1.count(10)) # 1
print(t1.count(100))  # 0 --> not present

### index()

print()
print(t1.index(10)) # 1
#print(t1.index(100)) # ValueError
print(t1.index(20,1,10))  # 1


####################

# append(),insert(),extend() and remove(), pop(), clear() is not applicable for Tuple because its immutable

