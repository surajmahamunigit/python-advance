# reverse()

list1=[10,20,30]
print("before: ", list1)
list1.reverse()
print("after: ", list1)

# output:
# before:  [10, 20, 30]
# after:  [30, 20, 10]


# reversed() : it same as reverse. but revered() is applicable to other collections.

list2=["raj","kumar","William"]
print("before: ", list2)

r = reversed(list2)  # returns -->     list_reverseiterator object

rev_list2 = list(r)  # very important
print("after: ", rev_list2)

# output:
# before:  ['raj', 'kumar', 'William']
# after:  ['William', 'kumar', 'raj']

s="durga"
rev_s = reversed(s)  # will return "reversed object"

for ch in rev_s:

    print(ch)

# output:
# a
# g
# r
# u
# d
