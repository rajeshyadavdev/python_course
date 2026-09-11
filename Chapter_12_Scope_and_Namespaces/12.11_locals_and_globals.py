""" 
Python provides two built-in functions to inspect namespaces.

Synatx:
  local()
  global()
  
1. locals() returns the current local namespace as a dictionary.
2. globals() returns the global namespace as a dictionary.
3. These are mainly used for debugging and learning.
4. Usually, we should not modify program logic using them.
"""

name = "Global"
def show():
  name = "Local"
  print(locals())
   
show()  

# {'name': 'Local'}

