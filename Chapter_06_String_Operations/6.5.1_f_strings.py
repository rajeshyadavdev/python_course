""" 
String Formatting
-----------------
String formatting means placing values inside a string in a clean way.
This is better than manually joining many values.

Python has three main ways to format strings:
● f-strings
● format()
● old % formatting


"""
# f-strings
# f-strings are the most readable and modern way.
# Write f before the string and place variables inside {}.

name = "Rajesh Yadav"
age = 22
print(f"My name is {name} and I am {age} years old.")
# My name is Rajesh Yadav and I am 22 years old.


# You can also place expressions inside f-strings.
a = 23
b = 20
print(f"Sum is {a + b}")
# Sum is 43


