# we will see how we can merge collections


def merge_lists():
    """
    Merge two or more list using (+) or [*list1,*list2]
    Args: None
    Returns: None
    """
    first_list=[1,2,3,4,5]
    second_list=[4,5,6,7,8]

    option=int(input("Add lists, Pick option 1 or 2: "))

    # Add lists using + operator
    if option==1:

        final_list=first_list+second_list
        print(f"Final list using + operator: {final_list}")

    # Use [*list1,*list2] to add two lists
    elif option==2:
         final_list=[*first_list,*second_list]
         print(f"Final list using [*list,*list2] : {final_list}")

    else:
        print("Please enter a valid option")




def merge_tuples():
    """
    Merge two or more tuple using (+) or (*tuple1,*tuple2)
    Args:None
    Return:None
    """

    first_tuple=(1,2,3,4,5)
    second_tuple=(4,5,6,7,8)

    option=int(input("Add tuples, Pick option 1 or 2: "))

    # Add two or more tuples using + operator
    if option==1:
        final_tuple=first_tuple+second_tuple
        print(f"Final tuple using + operator: {final_tuple}")

    # Add two tuples using (*tuple1, *tuple2)
    elif option==2:
        final_tuple=(*first_tuple,*second_tuple)
        print(f"Final tuple using (*tiple1,*tuple2): {final_tuple}")

    else:
        print("Please enter a valid option")




def merge_sets():
    """
    Merge two or more sets using {*set1,*set2}
    Args:None
    Returns:None
    """

    print("Using (+) operator will not work with sets")

    first_set={1,2,3,4,5}
    second_set={3,4,5,6,7}

    final_set={*first_set,*second_set}
    print("Final set: {}".format(final_set))


def merge_dictionary():
    """
    Merge two or more dictionaries using {**dict1,*dict2,**dict3}
    Args:None
    Returns:None
    """

    print("Using (+) operator will not work with dictionaries")

    first_dict={1:'A',2:'B',3:'C',4:'D',5:'E'}
    second_dict={3:'F',4:'G',5:'H',6:'I'}

    final_dict={**first_dict,**second_dict}
    print("Final dict: {}".format(final_dict))


# Add two list
merge_lists()
print()

# Add to Tuples
merge_tuples()
print()

# Merge sets
merge_sets()
print()

# Merge Dictionary
merge_dictionary()