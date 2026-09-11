""" 
int means integer. Integers are whole numbers. They do not have decimal points.
They can be negative as well as positive

example:- 
positive_number = 12
negative_number = -12
"""
age = 25
marks = 89
temperature = -10
zero_value = 0

print(f"Age:{age} and data type: {type(age)}")
print(f"Age:{marks} and data type: {type(marks)}")
print(f"Age:{temperature} and data type: {type(temperature)}")
print(f"Age:{zero_value} and data type: {type(zero_value)}")

# Age:25 and data type: <class 'int'>
# Age:89 and data type: <class 'int'>
# Age:-10 and data type: <class 'int'>
# Age:0 and data type: <class 'int'>


# int() is a function that convert string to int data type
# string must be number only not any character
string_number = "12"
int_number = int(string_number)
print(f"number:{int_number} and data type:{type(int_number)}")
# number:12 and data type:<class 'int'>