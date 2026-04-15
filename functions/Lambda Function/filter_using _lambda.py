# Method 1: using filter function without using lambda function

def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def filter_func(user_list):
   even_list=list(filter(is_even,user_list))
   return even_list

user_list=[1,2,3,4,5,6,7,8,9,10]

even_list=filter_func(user_list)
print(even_list)


# Method 2: using lambda function and filter function to find even numbers in the list

user_list=[1,2,3,4,5,6,7,8,9,10]
even_list=list(filter(lambda x:x%2==0,user_list))
print('even list:',even_list)

# Method 2: using lambda function and filter function to find odd numbers

user_list=[1,2,3,4,5,6,7,8,9,10]
odd_list=list(filter(lambda x:x%2==1,user_list))
print(f'odd list {odd_list}')

# Method 2: using lambda and filter to find actresses whos name starts with k
actresses=['kim','kimberly','kylie','jenny','cortney']

act_list=list(filter(lambda name:name.startswith('k'),actresses))
print(f'Actress list starting with k: {act_list}')