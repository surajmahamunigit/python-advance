import csv

def write_csv(filename):
    """ function to handle a csv file """

    with open('employee.csv','w',newline='') as f:
        w=csv.writer(f)

        w.writerow(['Employee ID','First Name','Last Name','Salary'])

        while True:
            employee_id=input('Enter employee ID: ')
            first_name=input('Enter first name: ')
            last_name=input('Enter last name: ')
            salary=input('Enter salary: ')
            w.writerow([employee_id,first_name,last_name,salary])

            option=input('Do you want to continue? (y/n): ')
            if option.lower()=='n':
                break

    print("Writing to the csv file completed")


def read_csv(filename):
    """ Function to read the csv file"""

    with open('employee.csv','r') as f:

        r=csv.reader(f)
        data=list(r)
        for row in data:
            for col in row:
                print(col,'\t\t',end='')
            print()



#write_csv('employee.csv')
read_csv('employee.csv')
