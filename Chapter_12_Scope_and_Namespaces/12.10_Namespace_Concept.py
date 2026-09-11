""" 
A namespace is a system that stores names and their related objects.

Syntax Idea
 name->object
 
1. A namespace maps names to values or objects.
2. Python uses namespaces to avoid name conflicts.
3. Different scopes have different namespaces.
4. Local, global, and built-in scopes each have their own namespaces.
5. The same name can exist in different namespaces without conflict. 
"""

x = 100
def show():
  x = 50
  print(x)

show()
print(x)
# 50
# 100

# 1. The global namespace has x = 100. The local namespace inside show() has x = 50.
# 2. Both names are x, but they belong to different namespaces.

''' 
Namespace             Contains
=========             ========
Local namespace       Names inside a function
Global namespace      Names created at file/program level
Built-in namespace    Python built-in names
Enclosing namespace   Names inside outer function.
'''
