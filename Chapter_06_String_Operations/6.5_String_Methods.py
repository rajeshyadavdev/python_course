""" 
String methods are built-in functions that work on strings.
Common string methods are used for cleaning, checking, changing case, finding text, and
replacing text.
"""

# lower()
# Converts string to lowercase.
text = "PYTHON"
print(text.lower()) # python


# upper()
# Converts string to uppercase.
text = "python"
print(text.upper()) # PYTHON


# strip()
# Removes extra spaces from the beginning and end.
text = "  python  "
print(text.strip()) # python


# replace()
# Replaces one part of a string with another.
text = "Coding with Java"
print(text.replace("Java","Python"))  # Coding with Python


# split()
# Splits a string into a list of parts using a separator.
text = "apple,banana,mango"
print(text.split(",")) # ['apple', 'banana', 'mango']


# find()
# Finds the position of a substring.
text = "Python"
print(text.find("th")) # 2
# If the text is not found, it returns -1.



# count()
# Counts how many times a character or substring appears.
text = "banana" 
print(text.count("a")) # 3



# startswith() and endswith()
text = "python"
print(text.startswith("py"),text.endswith("on")) # True True
# These methods are very useful in text checking and validation.
