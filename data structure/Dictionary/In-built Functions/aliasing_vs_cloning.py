

# -------------------------------
# Demonstrating setdefault()
# -------------------------------

student_scores={'a':1, 'b':2, 'c':3}

# Adds key if not present
print(student_scores.setdefault(4, 'd'))  # d

# Returns existing values if exists
print(student_scores.setdefault(1, 'F')) # a


# -------------------------------
# Aliasing Example
# -------------------------------

original_dict={1: 'a', 2: 'b', 3: 'c'}
alias_dict=student_scores  #  aliasing

alias_dict.setdefault(4,'F')
alias_dict.pop(2)
print(original_dict)   # {1: 'a', 3: 'c', 4: 'F'}  --> F added and B is gone


# -------------------------------
# Cloning Example
# -------------------------------

student_scores={1: 'a', 2: 'b', 3: 'c'}

cloned_dict=student_scores.copy()
print(cloned_dict)

cloned_dict.pop(1)
cloned_dict.popitem()

print("dict1:", student_scores)      # dict1:{1: 'a', 2: 'b', 3: 'c'}
print("dict2:", cloned_dict)      # dict2:{2: 'b'}
