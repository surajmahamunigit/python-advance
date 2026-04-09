# there are a multiple way we can create dictionary

## empty dictionary

d1={}

d2=dict()


# if we already have inputs

d3={10:"raj",20:"kumar",30:"William"}

print(d3) #{10:"raj",20:"kumar",30:"william"}
print(d3.keys()) # dict_keys([10, 20, 30])
print(d3.values()) # dict_values(['raj', 'kumar', 'William'])


# we can create dict from "list of tuples"

list1=[('name','raj'),('age',30),('city','LA')]

d4=dict(list1)
print(d4)  # {'name': 'raj', 'age': 30, 'city': 'LA'}


#we can create tuple from "list of lists"

list2=[['name','kenny'],['age',30],['city','LA']]

d5=dict(list2)
print(d5)  # {'name': 'kenny', 'age': 30, 'city': 'LA'}


#we can create dict from "tuple of tuples"

tup6=(('name','dennis'),('age:',30),('city','denver'))

d6=dict(tup6)
print(d6)  # {'name': 'dennis', 'age:': 30, 'city': 'denver'}


#we can create "tuple of lists"

t7=(["name",'namika'],['age',20],['city','pune'])

d7=dict(t7)
print(d7) # {'name': 'namika', 'age': 20, 'city': 'pune'}


#we can also create dict from "set of tuple"

s8={('name','raj'),('age',30),('city','LA')}

d8=dict(s8)
print(d8) # {'city': 'LA', 'age': 30, 'name': 'raj'}


#using dynamic input

d=eval(input("Enter the dictionary: "))
print(d)  # {'A': 100, 'B': 200, 'C': 300}



