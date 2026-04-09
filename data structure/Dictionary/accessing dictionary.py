dict1={1: "A", 2: "B", 3: "C"}

print(dict1[1]) # A
print(dict1[2]) # B
#print(dict[5])  --> KeyError

#always do this, so we dont get KeyError
key=int(input("Enter a number: "))

if key in dict1:
    print("For {} is in dict and its value is: {} ".format(key, dict1[key]))
else:
    print("Key is not in dict")



