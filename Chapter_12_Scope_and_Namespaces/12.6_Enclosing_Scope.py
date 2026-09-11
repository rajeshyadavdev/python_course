""" 
An enclosing scope exists when a function is defined inside another function.

Synatx:
    def outer_function():
        variable_name = value
        
        def inner_function():
            statement
            
1. Enclosing scope belongs to the outer function.
2. Inner functions can access variables from the outer function.
3. This scope is between local and global scope.
4. Enclosing scope is important for nested functions and closures.
            
"""

def outer_function():
    name = "Rajesh"
    
    def inner_function():
        print(name)
        
    inner_function()
    
outer_function()        
# Rajesh


