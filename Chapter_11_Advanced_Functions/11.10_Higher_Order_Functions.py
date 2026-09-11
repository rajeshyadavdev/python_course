""" 
A higher-order function is a function that does at least one of these:

1. Takes another function as an argument.
2. Returns another function.

def outer_function():
    def inner_function():
        statement
    return inner_function()
    
or 

def outer_function(function):
    return function()
    
    
 
Explanation
    1. Higher-order functions are possible because Python functions are objects.
    2. They are used in map(), filter(), reduce(), decorators, and callbacks.
    3. They make code flexible and reusable.
    4. They are common in functional programming.
            
"""
# Example 1: Function as Argument
def shout(text):
    return text.upper()

def process_text(function,text):
    return function(text)

result = process_text(shout,"Rajesh")
print(result) # RAJESH

# Here, process_text() is a higher-order function because it accepts another function.

