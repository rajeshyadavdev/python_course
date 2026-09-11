""" 
Syntax:
  dictinary_name.get(key)
  dictinary_name.get(key,defualt_value)
  
Explanation
  1. get() is used to access dictionary values safely.
  2. If the key exists, it returns the value.
  3. If the key does not exist, it returns None by default.
  4. We can also provide our own default value.
  5. get() avoids KeyError.  
"""
student = {
"name": "Aman",
"age": 21
}
print(student.get("name")) # Aman
print(student.get("marks")) # None
print(student.get("marks", "Not Available")) # Not Available



# [] vs get() Table
''' 
Access Method               If Key Exists                 If Key Missing
-------------               -------------                 --------------
student["name"]             Returns value                 Gives KeyError
student.get("name")         Returns value                 Returns None
student.get("marks", 0)     Returns value                 Returns default value
'''

