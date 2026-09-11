""" 
Strings in Python are immutable.
Immutable means: Once created, it cannot be changed directly.
"""

name = "Rajesh"

''' 
name  :  R  a   j   e   s   h
index :  0  1   2   3   4   5
'''
# Suppose we want to change R to K. This will not work:

# name[0] = "K"
# Error: TypeError: 'str' object does not support item assignment
# Why? Because strings cannot be changed character by character.

# Correct Way
first_name = "Rajesh"
first_name = "Rakesh"

print(first_name) # Rakesh

# Important understanding:
# Old string = "Rajesh"
# New string = "Rakesh"
# Python does not modify the old string. It creates a new string.


