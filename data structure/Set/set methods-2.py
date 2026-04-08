#################### lets see how to remove elements from the set ########

###### remove() ####

s1={1,2,3,4,5}
print(s1)  # {1, 2, 3, 4, 5}

s1.remove(1)
print(s1)  # {2, 3, 4, 5}

#s1.remove(90)
print(s1)  # 90 not present in set --> KeyError: 90 --> always check if element is present in set before removing
print()

######### discard()  ##########

s1={1,2,3,4,5}
print(s1)

s1.discard(5) # removes and returns 5
print(s1)  # {1, 2, 3, 4}

s1.discard(90)  #  no KeyError
print(s1)       # {1, 2, 3, 4}
print()


######### pop()  ##############

s1={1,2,3,4,5}
print(s1)

print(s1.pop()) # 2
print(s1.pop()) # 5
print(s1.pop()) # 3
print(s1.pop()) # 1
print(s1.pop()) # 4

#print(s1.pop()) # KeyError: 'pop from an empty set'

print()


######## clear() #######
s1={1,2,3,4,5}
print(s1)

s1.clear()
print(s1)  # set() --> returns empty set

