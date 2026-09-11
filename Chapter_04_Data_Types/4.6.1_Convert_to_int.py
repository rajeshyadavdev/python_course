""" 
int() converts a value into an integer.

"""

x = "100"
y = int(x)
print(f"X:{x},x-data-type:{type(x)} and Y:{y},y-data-type:{type(y)}")

# X:100,x-data-type:<class 'str'> and Y:100,y-data-type:<class 'int'>

# Before conversion: x = "100" type is str
# After conversion: y = 100 type is int

''' 
x = "100" ==> y = int(x) ==> y = 100
 str          convert          int  
'''

# Invalid int() Conversion

# This works:
number = int("50")
print(number,type(number))  # 50 <class 'int'>

# This does not work:
value = int("hello")
print(value,type(value))
# ValueError: invalid literal for int() with base 10: 'hello'
# Why ? Because "hello" is not a valid number.


string_float = int("10.5")
print(string_float,type(string_float))
# ValueError: invalid literal for int() with base 10: '10.5'
# Why? Because "10.5" is a decimal number written as a string. 
# It cannot be converted directly into int


