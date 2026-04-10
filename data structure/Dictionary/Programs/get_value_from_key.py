####### write a program to retrieve value for the given key

#user input
key=int(input("Enter the key: "))

#core logic

dict1={300:'D',400:'E',100:'F'}

if key in dict1:
    print("value is: ",dict1.get(key))

else:
    print("key is not present.")


######### 