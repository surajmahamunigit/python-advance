def write_file():
    """
    Function is used to show different write functions for the file
    """

    f=open('write.txt','w')

    # Write data to file using write()
    f.write('Raj \n')
    f.write('Kumar \n')
    f.write('Dennis \n')
    f.write('Claire \n')
    print('Finished writing data to file using write() function.')

    # Write data using writelines()

    toy_list=['bear\n','dog\n','doll\n']

    f1=open('write.txt','a')
    f1.writelines('Adding data to file using writelines() function.\n')
    f1.writelines(toy_list)
    print('Finished writing data to file using writelines function.')

    f1.close()

write_file()