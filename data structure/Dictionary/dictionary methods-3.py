########## pop() ######

#pop(key) will remove the item specified with the given key and return value

dict1={100:'A',200:'B',300:'C'}

print(dict1.pop(200)) #'B

print(dict1)  # {100: 'A', 300: 'C'}

#print(dict1.pop(700)) --> key=700 is not present. --> KeyError


######### pop(key, default_value) ############

dict1={100:'A',200:'B',300:'C'}

print(dict1.pop(100)) # 'A'

print(dict1.pop(800,"Key Not Present"))  # Key Not Present


