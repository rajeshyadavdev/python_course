""" 
**kwargs is used when we do not know how many keyword arguments will be passed.

Syntax:
    def function_name(**kwargs):
        statement

Explanation:
    1. **kwargs collects extra keyword arguments.
    2. The collected values are stored as a dictionary.
    3. Keys are argument names.
    4. Values are argument values.
    5. The name kwargs is a convention; the ** is important.

Flow Chart
==========
Function call has many keyword arguments
|
v
**kwargs collects them
|
v
Values are stored as a dictionary
        
"""

def show_profile(**details):
    for key,value in details.items():
        print(key,value)
        
show_profile(name="Rajesh",age=23,course="python")        

''' 
name Rajesh
age 23
course python
'''
# Here, details behaves like a dictionary.

