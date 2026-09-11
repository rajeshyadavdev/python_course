""" 
A closure is created when an inner function remembers variables from its outer function even after the outer function has finished.

Synatx:
    def outer_function():
        variable = value
        def inner_function():
            use variable
        return inner_function()
        
1. A closure needs a nested function.
2. The inner function uses a variable from the outer function.
3. The outer function returns the inner function.
4. The inner function remembers the outer variable.
5. Closures are useful for creating customized functions.
            
"""

def multiplier(number):
    def multiply(value):
        return value * number
    return multiply

double = multiplier(2)

print(double(5))  # 10
        