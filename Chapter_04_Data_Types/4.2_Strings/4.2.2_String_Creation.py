""" 
Strings can be created using quotes.
"""
# Using Double Quotes
name = "Rajesh Yadav"
print(f"My name is {name} and data type:{type(name)}")
# My name is Rajesh Yadav and data type:<class 'str'>


# Using Single Quotes
city_name = 'Delhi'
print(f"My city is {city_name} and data type:{type(city_name)}")
# My city is Delhi and data type:<class 'str'>

# Using Triple Quotes
message1 = """Python is easy.
python is simple, and 
python is user-friendly.
"""
print(f"What is python:{message1},data type:{type(message1)}")
# What is python:Python is easy.
# python is simple, and 
# python is user-friendly.
# ,data type:<class 'str'>


message2 = '''Python is easy.
python is simple, and 
python is user-friendly.
'''
print(f"What is python:{message2},data type:{type(message2)}")
# What is python:Python is easy.
# python is simple, and 
# python is user-friendly.
# ,data type:<class 'str'>



# Empty String
# A string can also be empty.

name = "" 
print(name,type(name)) 
#  <class 'str'>

# There is no visible text in the output because the string is empty.
