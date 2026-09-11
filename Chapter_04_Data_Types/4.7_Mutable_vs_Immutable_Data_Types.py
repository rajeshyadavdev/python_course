""" 
This is a very important concept in Python. First understand these two words:

Mutable = Can be changed after creation

Immutable = Cannot be changed after creation


Immutable Data Types:
---------------------
Immutable data types cannot be changed directly after they are created. 

Examples of immutable data types:

● int
● float
● complex
● str
● bool
● NoneType

We have already studied these types in this chapter


immutable value is created.
 |
Cannot change the same value directly.
 |
Python create new value if needed.  
"""

name = "Ravi"
name[0] = "K" #TypeError: 'str' object does not support item assignment
# Because string is immutable.

# Correct idea:
first_name = "Ravi"
first_name = "Kavi"
# Output: Kavi

# Here, Python does not change "Ravi" directly. It creates a new string "Kavi" and makes name refer to that new str


# Immutable Number Example
# Numbers are also immutable.

age = 10
age = 12
print(age) # first age=10 then age=12 


''' 
Mutable Data Types
------------------
Mutable data types can be changed after creation. Some mutable data types in Python are:
● list
● dictionary
● set

These will be studied in detail later in the Data Structures section.For now, only remember:
1. Mutable objects can be modified.
2. Immutable objects cannot be modified directly.


int         =>Immutable

float       =>Immutable

complex     =>Immutable

str         =>Immutable

bool        =>Immutable

NoneType    =>Immutable

list        =>Mutable

dict        =>Mutable

set         =>Mutable
'''
