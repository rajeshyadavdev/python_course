""" 
Scope means the area of a program where a variable can be accessed.
Namespace means a place where names are stored and mapped to objects.

name -> object/value
Example: x = 10
Here, Python stores the name x and connects it to the value 10.


A local scope is created inside a function. 
Variables created inside a function are local variables.

Synatx:
    def function_name():
        variable_name = value

Explanation:
    1. A local variable is created inside a function.
    2. It can be used only inside that function.
    3. It cannot be accessed directly outside the function.
    4. Local variables are created when the function is called.
    5. They are destroyed after the function finishes.

"""

def show_name():
    name = "Rajeh"
    print(name)
    
show_name()
# Rajesh

# If we call name here we get error
# print(name)  "name" is not defined
