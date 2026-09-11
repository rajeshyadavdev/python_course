""" 
A data type tells Python what kind of value a variable is storing.

Simple meaning: Data type = Type/category of data stored in a variable

Value -> Python check what kind of value is it -> Assign a data type
"""

name = "Rajesh Yadav"
age = 27
price = 120.50
is_active = True

''' 
name => Variable name,  "Rajesh Yadav" => Value  and DataType => String
age => Variable name,  27 => Value  and DataType => Integer
price => Variable name,  120.50 => Value  and DataType => Float
is_active => Variable name,  True => Value  and DataType => Boolean
'''

print(f"Value:{name} and Data Type:{type(name)}")
print(f"Value:{age} and Data Type:{type(age)}")
print(f"Value:{price} and Data Type:{type(price)}")
print(f"Value:{is_active} and Data Type:{type(is_active)}")

# Value:Rajesh Yadav and Data Type:<class 'str'>
# Value:27 and Data Type:<class 'int'>
# Value:120.5 and Data Type:<class 'float'>
# Value:True and Data Type:<class 'bool'>

