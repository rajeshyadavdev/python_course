""" 
Advanced functions help us write more flexible, reusable, and compact code.

Before starting, remember:

In Python, functions are objects. This means:

1. A function can be stored in a variable.
2. A function can be passed as an argument.
3. A function can be returned from another function.
4. A function can be written inside another function.


Synatx:
    def function_name():
        statement
    
    new_name = function_name
    
In Python, functions behave like normal objects. 
We can store a function in a variable and call it using that variable.
   
   
"""
def greet():
    print("Hello World!")
    
message = greet
message()    # Hello World!

# Here, message refers to the same function as greet.