""" 
When using different types of parameters together, the order matters.

Syntax:

def function_name(normal_parameter,default_parameter=value,*args,**kwargs):
    statement
    
Explanation
    1. Normal parameters come first.
    2. Default parameters come after normal parameters.
    3. *args comes after normal/default parameters.
    4. **kwargs comes last.
    5. This order keeps function calls clear and valid. 
"""

# Parameter Order Table
''' 
Order   Parameter Type          Example
1       Normal parameter        name
2       Default parameter       age=18
3       *args                   *marks
4       **kwargs                **details
'''

def show_details(name,age=18,*marks,**details):
    print("Name:",name)
    print("Age:",age)
    print("marks:",marks)
    print("Details:",details)
    
show_details("Rajesh",22,60,89,69,city="Delhi",state="Bihar")    
''' 
Name: Rajesh
Age: 22
marks: (60, 89, 69)
Details: {'city': 'Delhi', 'state': 'Bihar'}
'''

