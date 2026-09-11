""" 
Syntax:
  new_dict = old_dict.copy()
  
Explanation
  1. copy() creates a shallow copy of a dictionary.
  2. Direct assignment does not create a new dictionary.
  3. Direct assignment makes both variables point to the same dictionary.  
"""

# Direct Assignment Example
student1 = {"name": "Aman", "age": 21}
student2 = student1
student2["age"] = 22
print(student1) # {'name': 'Aman', 'age': 22}
print(student2) # {'name': 'Aman', 'age': 22}




# Real Copy Example
student1 = {"name": "Aman", "age": 21}

student2 =  student1.copy()

student2["age"] = 33

print(student1) # {'name': 'Aman', 'age': 21}
print(student2) # {'name': 'Aman', 'age': 33}


''' 
Copying Table
-------------
Method              Creates New  Dictionary?          Notes
------              -----------------------           -----
dict2 = dict1           No                            Same dictionary reference
dict2 = dict1.copy()    Yes                           Shallow copy
dict2 = dict(dict1)     Yes                           Shallow copy
'''

