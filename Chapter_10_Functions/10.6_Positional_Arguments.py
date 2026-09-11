""" 
Positional arguments are matched based on their position.

Synatx:
    function_name(argument1, argument2)

Explanation
    1. Python passes arguments in the same order as parameters.
    2. The first argument goes to the first parameter.
    3. The second argument goes to the second parameter.
    4. Order matters in positional arguments.

"""

def details(name,age):
    print(f"Name {name} and Age {age}")
    
details("Rajesh",26)    
# Name Rajesh and Age 26