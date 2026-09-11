""" 
A function decorator is used to add extra behavior to a function.

Syntax:
  def decorator_name(func):
    def wrapper():
      extra_code
      func()
      extra_code
  return wrapper()    
"""
def my_decorator(func):
  def wrapper():
    print("Before function")
    func()
    print("After function")
  return wrapper
@my_decorator
def greet():
  print("Hello")

greet()
''' 
Before function
Hello
After function


1. my_decorator receives greet. wrapper adds extra behavior.
2. greet() now actually calls wrapper(). Inside wrapper, the original greet() is called.
'''