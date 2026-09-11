""" 
Membership operators are used to check whether a value exists inside another value.

Python has two membership operators:
1. in
2. not in

For now, we will use membership operators with strings because strings are already
covered.

"""

# in Operator
# The in operator checks whether something is present.

text = "Python"
print("P" in text)   # True
print("Py" in text)  # True
print("Java" in text)# False

''' 
Explanation:
"P" exists in "Python"      => True
"Py" exists in "Python"     => True
"Java" does not exist       => True
'''

# not in Operator
# The not in operator checks whether something is not present.
ext = "Python"
print("Java" not in text) # True
print("Py" not in text)   # False


# Membership Is Case-Sensitive
# Python checks uppercase and lowercase carefully.
text = "Python"
print("P" in text)  # True
print("p" in text)  # False

# "P" and "p" are different in Python.

