""" 
The type() function is used to check the data type of a value or variable.

synatx : type(value)
"""

name = "Rajesh"
print(type(name)) # <class 'str'>

age = 24
print(type(age)) # <class 'int'>

price = 2020.49
print(type(price)) # <class 'float'>

is_active = True
print(type(is_active)) # <class 'bool'>

data = None
print(type(data)) # <class 'NoneType'>

number = 3 + 4j
print(type(number)) # <class 'complex'>

''' 
variable => type(value) => Python tell the data type
'''