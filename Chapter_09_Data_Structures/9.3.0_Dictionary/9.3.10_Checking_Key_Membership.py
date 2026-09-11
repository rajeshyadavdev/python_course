""" 
Syntax:

key in dictionary

key not in dictionary


Explanation
  1. in checks whether a key exists in the dictionary.
  2. It checks keys, not values.
  3. It returns True or False.
"""
students = {"name":"Rajesh","age":23,"city":"Delhi"}
print("name" in students)  # True
print("age" not in students) # False
print("course" in students)  # False


# Membership Table
''' 
Code                    Meaning
----                    --------
"name" in student       Checks if key exists
"marks" not in student  Checks if key does not exist
"Aman" in student       Checks key, not value
'''