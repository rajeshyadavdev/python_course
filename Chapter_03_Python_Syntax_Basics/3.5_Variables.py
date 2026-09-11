"""
Variables
---------
A variable is a name used to store data.

Basic syntax: variable_name = value

"""

name = "Rajesh"
age = 29
height = 5.9
print(f"Your name is {name}, age is {age} and height is {height}")

# Output:
# Your name is Rajesh, age is 29 and height is 5.9

''' 
name is variable name and its contain value Rajesh
age is variable name and its contain value 29
height is variable name and its contain value 5.9
'''

city = "Delhi"
marks = 89
is_passed = True

''' 
city => variable name,  value => "Delhi" and variable type => String
marks => variable name,  value => 89 and variable type => Integer
is_passed => variable name,  value => True and variable type => Boolean
'''


# Python Variables Do Not Need Type Declaration
# In Python, we do not need to write the data type before the variable name.

x = 10
print(x) # 10

x = "Hello World!"
print(x) # Hello World!
# In the first line, x stores an integer. Later, x stores a string. This is allowed because Python is dynamically typed.


# Multiple Variable Assignment
a,b,c = 10,20,30
print(f"a:{10}, b:{b} and c:{c}") # a:10, b:20 and c:30



# Same Value to Multiple Variables
p = q = r = 10
print(f"p:{p}, q:{q} and r:{r}") #p:10, q:10 and r:10

