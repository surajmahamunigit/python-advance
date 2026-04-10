# Program: write a program to calculate the number of occurrences of each letter within given string.

input_string=input("Enter the string: ")

char_frequency={}

# Iterate over each letter
for letter in input_string:

    # Check if the letter exist, if exist -> add +1, or add letter to dictionary
    char_frequency[letter]= char_frequency.get(letter, 0) + 1

# Print the output
for letter,count in char_frequency.items():
    print(letter,'->',count)


# Output:
# Enter the string: ADKSFKND
# A -> 1
# D -> 2
# K -> 2
# S -> 1
# F -> 1
# N -> 1
