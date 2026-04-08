list1=[10,20,[30,40]]
print("list o/p: ", list1)  # list o/p:  [10, 20, [30, 40]]

### matrix style list

list2=[[10,20,30],[40,50,60],[78,80]]

print("Printing list row-by-row: ")

for x in list2:
    print(x)

    # output:
    # Printing list row - by - row:
    # [10, 20, 30]
    # [40, 50, 60]
    # [78, 80]

print("Printing list matrix style:")

for x in list2:

    for y in x:
        print(y, end=' ')

    print()

# output:
# Printing list matrix style:
# 10 20 30
# 40 50 60
# 78 80