gl_var1 = 100
gl_var2 = 200

def local_global_var():
    local_var1 = 9
    local_var2 = 99
    global gl_var1
    gl_var1=19


    print(f"global varaible 1:{gl_var1} ")
    print(f'global varaible 2:{gl_var2} ')
    print(f'local varaible 1:{local_var1} ')
    print(f'local varaible 2:{local_var2} ')


local_global_var()