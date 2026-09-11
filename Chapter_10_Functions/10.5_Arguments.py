""" 
An argument is the actual value passed to a function during function call.

Synatx:
    function_name(argument)
    
Explanation
    1. Parameter is written in function definition.
    2. Argument is passed during function call.
    3. Arguments provide real values to parameters.    
    

Parameter vs Argument
=====================
Term        Where It Appears                Meaning
----        ----------------                -------
Parameter   Function definition             Variable that receives value
Argument    Function call                   Actual value passed
"""
def greet(name):
    print(f"Welcome {name}")
    
greet("Rajesh")    
# Welcome Rajesh

# name => Parameter
# "Rajesh" => Argument
