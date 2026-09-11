""" 
A default parameter has a predefined value. 
If no argument is passed, the default value is used.

Syantax:
    def function_name(parameter=default_value):
        statement
        
1. Default parameters make arguments optional.
2. If an argument is provided, Python uses the given value.
3. If no argument is provided, Python uses the default value.
4. Non-default parameters must come before default parameters.

"""
def greet(name="Guest"):
    print(f"Hello {name}") 
    
greet("Rajesh")    
greet()    

# Hello Rajesh
# Hello Guest

# Correct and Incorrect Order
''' 
Code                            Valid?  Reason

def show(name, age=18):         Yes     Default parameter comes after normal parameter
def show(name="Guest", age=18): Yes     Both have defaults
def show(name="Guest", age):    No      Non-default parameter cannot come after

'''
# Important Warning: Avoid Mutable Default Values
# Do not use mutable objects like list or dictionary as default values.


# Wrong style:
def add_items(item,items=[]):
    items.append(item)
    
    return items

print(add_items("A")) # ['A']
print(add_items("B")) # ['A', 'B']


# The same list is reused between function calls.

def add_items2(item,items=None):
    if items is None:
        items = []
    items.append(item)  
    return items

print(add_items2("A"))   # ['A']
print(add_items2("B"))   # ['B']

