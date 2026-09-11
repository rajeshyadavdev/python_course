""" 
A nested function is a function defined inside another function.

Synatx:
    def outer_function():
        def inner_function():
            statement
        
        inner_function()

1. A nested function is created inside another function.
2. The inner function can be used only inside the outer function.
3. Nested functions are useful for hiding helper logic.
4. They are also used in closure    
"""

def outer_function():
    print("Outer function started")
    def inner_function():
        
        print("Inner function started")

    inner_function()
    
outer_function()    
        
# Outer function started
# Inner function started

# Important point: inner() cannot be called directly outside outer().
