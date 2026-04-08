
list1 = [x for x in range(0,11)]  # will create a list with 1-10 values
print(list1)   #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# create a list with square values of 1-10
list2 = [x*x for x in range(1,11)]
print(list2)    #  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# create a list with power of 2.
list3 = [2**x for x in range(1,6)]     # its 2 ** x
print(list3)   #  [2, 4, 8, 16, 32]


# numbers divisible bt 10
list4 = [x for x in range(1,101) if x%10==0 ]
print(list4)  #  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# create a list with elements present in list1 but not in list2
list1=[10,20,30]
list2=[30,40,50]

list3 = [x for x in list1 if x not in list2]
print(list3)   #  [10, 20]


# create a list with elements present in both the lists
list4 = [x for x in list1 if x in list2]
print(list4)  # [30]


# create a list with only first word from the given list
list1=["Ram", "Amy", "Raj", "Kiran"]

list2= [word[0] for word in list1]
print(list2)   #  ['R', 'A', 'R', 'K']


#
str1="the quick brown fox jumps over the lazy dog"

#step 1: split the words
list1=str1.split()
print(list1)  # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

#step 2: [['THE',3],["QUICK',5]...]
list2= [[word.upper(), len(word)] for word in list1]
print(list2)  #  [['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]



