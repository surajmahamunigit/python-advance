############## setdefault(key, default_value)  #################

dict1={'a':1,'b':2,'c':3}

print(dict1.setdefault(4,'d'))  # d

print(dict1.setdefault(1,'F')) # a --> returned the original key value


############  Aliasing ##########

dict1={1:'a',2:'b',3:'c'}
dict2=dict1  #  aliasing

dict2.setdefault(4,'F')
dict2.pop(2)
print(dict1)   # {1: 'a', 3: 'c', 4: 'F'}  --> F added and B is gone


############## cloning ########

dict1={1:'a',2:'b',3:'c'}

dict2=dict1.copy()
print(dict2)

dict2.pop(1)
dict2.popitem()

print("dict1:",dict1)      # dict1:{1: 'a', 2: 'b', 3: 'c'}
print("dict2:",dict2)      # dict2:{2: 'b'}
