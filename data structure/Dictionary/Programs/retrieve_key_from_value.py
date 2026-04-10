# write a program to retrieve key based on the value

#so far we have retrieve value based on key. its easy and we can do it multiple ways
#dict1[key]

#if key in dict1:
#   print(dict1.get(key))
#else:
#   print("key doesnt exist")

#but we dont have any direct way to get key based on given value

value=input("Enter the value: ")

# core logic

dict1={100:'A',300:'C',400:"D",200:"B"}

available=False

#traverse over every item in dict and look for value
for k,v in dict1.items():

    #if given value is present in item(k,v), then return key for the given value
    if v==value:
        print("Corresponding key is: ",k)
        available=True

if available==False:
    print("Value is not present.")