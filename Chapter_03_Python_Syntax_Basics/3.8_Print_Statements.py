"""
Print Statements
----------------
The print() function is used to display output on the screen.


"""

# Basic Print
print("Hello, World!")
# 


# Printing Numbers
print(10)  # 10
print(10.23) # 10.23



# Printing Variables
name = "Rakesh"
age = 26
print("Name:",name,"Age:",age)
# Name: Rakesh Age: 26


# Using f-strings
# f-strings are a clean way to insert variables inside text.
city = "Delhi"
is_student = True
print(f"City {city} and students {is_student}")
# City Delhi and students True



# Print with Separator
# The sep parameter controls how multiple values are separated.
# Default seperator is space
print("Python","Java","JavaScript",sep="|")
# Python|Java|JavaScript


# Print with End Parameter
# By default, print() moves to a new line after printing.
# Defualt end is new line \n
print("Hello",end=" ")
print("World!")
# Hello World!!


# Example
print("A",end="-")
print("B",end="-")
print("C")
# A-B-C