"""
Syntax
    def function_name():
        statement
        
1. def is used to define a function.
2. The function name comes after def.
3. Parentheses () are required.
4. A colon : marks the start of the function body.
5. The function body must be indented.


def     function            ()          :
|           |               |           |
keyword     name        parentheses   colon  
"""
def say_hello():
    print("Hello!")
    
# This only defines the function. It does not run yet. To run it, we must call it.
say_hello() 
# Hello!

# Empty Function
# If we want to create a function but write logic later, use pass.
def future_function():
    pass


