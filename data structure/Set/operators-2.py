########### set specific methods ########

#### union() or | ###

s1={1,2,3}
s2={3,4,5}

s3=s1.union(s2)  # or s3= s1 | s2
print(s3)  # {1, 2, 3, 4, 5}
print()

########  intersection() or & #########

s1={1,2,3}
s2={3,4,5}

s3=s1.intersection(s2) # or s3= s1 & s2
print(s3)  # {3}
print()


####### difference() or - #######3

s1={1,2,3}
s2={3,4,5}

s3= s1.difference(s2) # or s3 = s1 - s2
print(s3)  # {1, 2}
print()


####### symmetric_difference() or ^ ########

s1={1,2,3}
s2={3,4,5}

s3= s1.symmetric_difference(s2) # or s3= s1 ^ s2
print(s3)  # {1, 2, 4, 5}
print()