""" 
A global scope is the main area of the program. 
Variables created outside all functions are global variables.

Synatx:
    variable_name = value
    def function_name():
        statement
        
Explanation:
    1. A global variable is created outside functions.
    2. It can be accessed inside functions.
    3. It can also be accessed outside functions.
    4. Reading a global variable inside a function does not require the global keyword.
    5. To modify a global variable inside a function, we need the global keyword.
        
"""
course = "Python"
def show_course():
    print(course)
    
show_course()
print(course)   

# Python 
# Python

# NOTE: Global variables are accessible throughout the file after they are defined.
 