""" 
A parameter is a variable written inside the function definition. 
It receives values when the function is called.

Syntax:
 def function_name(parameter):
    statement
   
   
Explanation
    1. Parameters make functions flexible.
    2. Parameters allow us to send data into a function.
    3. A function can have one or more parameters.
    4. Parameters are written inside parentheses during function defination.    
    
    
Flow Chart
==========
Function definition has parameter
|
v
Function call sends value
|
v
Parameter receives value
|
v
Function uses that value    

"""

def greet(name):
    print(f"Hello {name}.")
    
greet("Rajesh")    
# Hello Rajesh.

# Here, name is a parameter.

