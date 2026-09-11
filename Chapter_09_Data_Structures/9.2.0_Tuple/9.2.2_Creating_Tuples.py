""" 
Syntax:
  tuple_name = (item1, item2, item3)

1. Tuples can store numbers, strings, Booleans, or mixed values. An empty tuple can
also be created.

2. A tuple can be created with or without parentheses, but parentheses are
recommended for clarity.

3. A single-item tuple must have a comma.
"""
numbers = (10, 20, 30)
names = ("Aman", "Riya", "Kabir")
mixed = ("Python", 100, 99.5, True)
empty_tuple = ()

print(numbers)      # (10, 20, 30)

print(names)        # ('Aman', 'Riya', 'Kabir')

print(mixed)        # ('Python', 100, 99.5, True)

print(empty_tuple)  # ()




# Different Ways to Create Tuples
# Empty tuple 
empty = ()
print(empty) # ()


# Number tuple
marks = (80, 90, 75)
print(marks) # (80, 90, 75)

# String tuple 
names = ("Aman", "Riya")
print(names) # ('Aman', 'Riya')

# Mixed tuple 
data = ("Aman", 20, True)
print(data) # ('Aman', 20, True)

# Nested tuple 
matrix = ((1, 2), (3, 4))
print(matrix) # ((1, 2), (3, 4))

# Without parentheses 
items = 10, 20, 30
print(items) # (10, 20, 30)


# Using tuple() 
letters = tuple("ABC")
print(letters) # ('A', 'B', 'C')