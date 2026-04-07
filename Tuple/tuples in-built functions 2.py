### reverse() --> tuple is immutable --> AttributeError

### sort() --> tuple is immutable  --> AttributeError

############## reversed()

t1= (10,20,30, 'durga')

r=reversed(t1)  # --> returns reversed object
print(r)

rev_t1=tuple(reversed(t1)) # --> returns reversed t1
print(rev_t1)   #  ('durga',30, 20, 10)


############ sorted

t2=(400, 100,200,500,900)
list2=sorted(t2)
print(list2)  # returns list object --> [100, 200, 400, 500, 900]

sorted_t2=tuple(sorted(t2)) # --> (100, 200, 400, 500, 900)
print(sorted_t2)