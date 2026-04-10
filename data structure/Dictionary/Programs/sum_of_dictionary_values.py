def calculate_total_marks(student_marks):
    """
    Calculate the sum of all student marks.

    Args:
        student_marks (dict): Dictionary with student names as keys and marks as values

    Returns:
        int: Total marks
    """
    total_marks = 0

    for name, marks in student_marks.items():
        total_marks += marks

    return total_marks


# Example usage
students = {
    'kumar': 92,
    'sheila': 93,
    'randy': 84,
    'dennis': 65
}

# Method 1: Using custom function
total = calculate_total_marks(students)
print("Total marks (manual):", total)

# Method 2: Using built-in function
print("Total marks (using sum):", sum(students.values()))