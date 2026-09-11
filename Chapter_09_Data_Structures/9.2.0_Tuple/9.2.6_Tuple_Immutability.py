""" 
Syntax:
    tuple_name[index] = new_value

This syntax is not allowed for tuples.

Explanation
    1. Tuples are immutable.
    2. Once a tuple is created, its values cannot be changed directly.
    3. We cannot update, add, or remove tuple items directly.
    4. If changes are needed, use a list or create a new tuple.
"""
numbers = (10, 20, 30)
# numbers[1] = 25 # TypeError: 'tuple' object does not support item assignment

# Correct Way--> Create a new tuple:
numbers = (10, 20, 30)
numbers = (10, 25, 30)
print(numbers) # (10, 25, 30)


# Memory Idea
# Before: numbers ----> (10, 20, 30)
# After: numbers ----> (10, 25, 30)
# The old tuple is not changed. The variable starts pointing to a new tuple.





