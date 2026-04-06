#remove(element)

l=[10,20,30]
print(l.pop())       # 30 --> removes the last element and returns it
print(l)  # [10,20] last element is gone

print(l.pop())  # 20
print(l.pop())  # 10
print(l)        # []

# print(l.pop())  -> IndexError


# pop(index)
# we can also remove element from specified index
l1=[10,20,30]

print(l1.pop(1)) # 20
print(l1)        # [10,30] --> element at index 1 is gone

# print(l1.pop(100000))  #IndexError: pop index out of range


