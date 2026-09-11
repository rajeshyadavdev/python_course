""" 
Slicing means taking a part of a string.

Syntax:
string[start:stop:step]

Important rule: the start index is included, and the end index is excluded.

"""

word = "Python"
print(word[0:3]) # Pyt
print(word[2:])  # thon
print(word[:4])  # Pyth


# You can also use step values:
print(word[0:6:2])  # Pto


# To reverse a string:
print(word[::-1])  # nohtyP

# Because it start from right side

