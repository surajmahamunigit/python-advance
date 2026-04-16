def read_function():
    """
    Read the file data using read(), read(n), readline() and readlines() function
    """

    # read()
    print('Reading file using read() function:')

    f=open('abc.txt','r')
    data=f.read()
    print(data)
    f.close()

    # read(n)
    print('Reading file using read(n) function:')
    ch_num=int(input('Enter how many characters of you want to read: '))

    f=open('abc.txt','r')
    data=f.read(ch_num)
    print(data)
    f.close()

    # readline() --> used to read only one line but lets use it to read whole file
    print('Reading file using readline() function:')
    f=open('abc.txt','r')
    line=f.readline()

    while line != '':
        print(line,end='')
        line=f.readline()

    f.close()

    # readlines()
    print('Reading file using readlines() function:')
    f=open('abc.txt','r')
    lines=f.readlines()

    for line in lines:
        print(line,end='')

    f.close()





read_function()