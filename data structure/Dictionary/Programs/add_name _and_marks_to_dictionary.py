#write a program to enter student name and marks in the dictionary

#user input
num=int(input("Enter the number of students: "))

#core logic

d={}

for student in range(1,num+1):
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))

    d[name]=marks

print('name','\t\t','marks')

for key in d:
    print(key,'\t\t',d[key])

# o/p:
# name 		 marks
# ram 		 89
# sheila 		 87
