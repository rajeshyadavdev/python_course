""" 
Identity operators are used to check whether two variables refer to the same object in
memory.

Python has two identity operators:
1. is
2. is not

Important:
== checks value

is checks identity/memory object.
"""

# is Operator
# The is operator checks whether two variables point to the same object.

a = None
b = None
print(a is b) # True

''' 
Explanation:
a refers to None
b refers to None
Both refer to the same None object.
'''

# is not Operator
# The is not operator checks whether two variables do not point to the same object.
a = None
b = 10
print(a is b) # False
''' 
Explanation:
a refers to None
b refers to 10
They are not the same object.
'''

# Difference Between == and is
# == checks whether values are equal.
# is checks whether both variables refer to the same object.
a = 100
b = 100
print(a == b) # True
print(a is b) # True
''' 
For some simple values, Python may reuse the same object internally.
But beginners should remember this rule: Use == for value comparison. Use is mainly with None

'''
result = None
print(result is None)      # True
print(result is not None)  # False
