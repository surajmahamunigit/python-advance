

def properties():

    """
    Practice different file object properties
    """

    f=open('abc.txt','r')

    # file name
    print(f'File name: {f.name}')

    # mode
    print(f'Mode in which file is opened: {f.mode}')

    # closed
    print('Is file closed: {f.closed})')

    # readable or writable
    print('Is file opened in readable mode: {f.readable()}')
    print('Is file opened in writeable mode: {f.writable()}')

    # close the file
    f.close()
    print('Is file closed: {f.closed})')


properties()