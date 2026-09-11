""" 
Synatx:
  for item in set_name:
    statement
    
    
Explanation
    1. Sets do not support indexing.
    2. Sets do not support slicing.
    3. Values can be accessed by looping.
    4. Membership can be checked using in.

"""

languages = {"Python", "Java", "C++"}
for item in languages:
    print(item)
    
''' 
C++
Java
Python
'''    
# Output order may differ.



# Invalid Access:
languages = {"Python", "Java", "C++"}
print(languages[0]) # TypeError: 'set' object is not subscriptable



# Accessing Table
''' 
Operation                   Allowed?                Example
---------                   -------                 -------
Looping                     Yes                     for item in items:
Membership check            Yes                     "Python" in items
Indexing                    No                      items[0]
Slicing                     No                      items[1:3]
'''
