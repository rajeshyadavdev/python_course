""" 
__call__ allows an object to be called like a function.

Syntax
  def __call__(self):
    statement

Explanation
1. __call__ runs when an object is called using parentheses.
2. It makes an object callable.
3. It is useful when an object stores data and also performs an action.
4. It is commonly used in decorators, callbacks, and callable classes.
"""
class Greeter:
  def __init__(self, name):
    self.name = name

  def __call__(self):
    print("Hello", self.name)

greet_aman = Greeter("Aman")
greet_aman()
# Hello Aman

