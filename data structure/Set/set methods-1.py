s1={1,2,3,4,}
s2={10,30,40}

#len():
print(len(s1))  # 4

############## lets see how to add elements in set #############

#add():
s1.add(10)
print(s1)  # {1, 2, 3, 4, 10}

list1=[100,200,300]
#s1.add(list1)         # TypeError --> can add list,set


#update(): we can add multiple iterable objects
s1={1,2,3,4,}
list1=[100,200,300]
s1.update(list1)     # --> adding list to the set
print(s1)    # {1, 2, 3, 100, 4, 200, 300}

s1={1, 2, 3, 4, 5}
s1.update(s2)  # --> adding set to the set
print(s1)   # {1, 2, 3, 4, 5, 40, 10, 30}

s1={1, 2, 3, 4, 5}
t1=(111,222,333,444)
s1.update(t1)  # --> adding tuple to the set
print(s1)   # {1, 2, 3, 4, 5, 333, 222, 111, 444}  --> we can add tuple but not list,set,dict

s1={1,2,3,4,}
s1.update(range(1,6), range(11,16))
print(s1)      #  {1, 2, 3, 4, 5, 11, 12, 13, 14, 15}  --> duplicates not allowed
