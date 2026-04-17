def directory_functions():
    """ This function implements to different Directory functions"""

    import os

    # Current working directory
    cwd=os.getcwd()
    print(f'Current working directory is: {cwd}')

    # Create a directory in the current directory
    os.mkdir('dir1')
    print("directory is created.")

    # create directory inside directory from current directory
    os.mkdir('dir1/dir2')
    print('Successfully created sub-directory')

    # To create multiple directories:
    os.makedirs('dir2/dir3/dir4')
    print('Successfully created sub-directories')

    # To remove directory or sub-directory
    os.rmdir('dir1/dir2')
    print('Successfully removed sub-directories')
    os.rmdir('dir1')

    # To remove multiple directories in the path
    os.removedirs('dir2/dir3/dir4')
    print('Successfully removed all sub-directories')



# Testing different directory functions
directory_functions()