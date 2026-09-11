""" 
If the decorated function has arguments, the wrapper should accept *args and **kwargs.

Syntax:
def decorator_name(func):
  
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  
  return wrapper

"""