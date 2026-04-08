# write a program to find unique vowels present in the given string

str1 = input("Enter the string: ")

##### Using List Comprehension  ########

vowels=['a','e','i','o','u']

result= [ch for ch in vowels if ch in str1]

print(result)  # apple software --> ['a', 'e', 'o']


# we can write this program other way too
result=[]

for ch in vowels:
    if ch in str1:
        result.append(ch)

print(result)  # "apple software" --> ['a', 'e', 'o']
