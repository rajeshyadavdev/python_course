""" 
A decorator is a function that takes another function and adds extra behavior to it without
changing the original function code.

Basic Idea
==========
Decorator = function that modifies/enhances another function

Synatx:
  @deorator_name
  def funtion_name():
    statement
    
function_name = decorator_name(funtion_name)  


1. Decorators are based on functions being first-class objects.A decorator takes a function as input.
2. It usually defines an inner wrapper function. It returns the wrapper function.
3. The wrapper adds extra behavior before or after the original function.
  

Flow Chart
==========
Original function
|
v
Decorator receives function
|
v
Wrapper adds extra behavior
|
v
Decorated function is returned  
"""