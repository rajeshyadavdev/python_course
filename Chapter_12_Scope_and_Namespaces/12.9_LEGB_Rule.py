""" 
LEGB is the order Python follows while searching for a variable name.
L -> Local
E -> Enclosing
G -> Global
B -> Built-in

When Python sees a variable name, it searches in this order:

1. Local scope: inside the current function.
2. Enclosing scope: inside outer functions.
3. Global scope: main program/file.
4. Built-in scope: built-in Python names.

"""
x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print(x)
  inner()

outer()
# local

# Output: local ⇒ Python finds x in the local scope first, so it does not search further.


''' 
Search Order   Scope            Example
============   ======           =======
1              Local            Variable inside current function
2              Enclosing        Variable inside outer function
3              Global           Variable outside functions
4              Built-in         print, len, type
'''
