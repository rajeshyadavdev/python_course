""" 
Syntax
  dictionary_name[key]

Explanation
  1. Dictionary values are accessed using keys.
  2. Unlike lists and tuples, dictionaries are not accessed mainly by index.
  3. If the key exists, Python returns its value.
  4. If the key does not exist, Python gives KeyError.

"""
student = {
  "name":"Rajesh",
  "age":23,
  "course":"Python"
}
print(student["name"]) # Rajesh
print(student["age"])  # 23



# Accessing Table
''' 
Code                Meaning         Result
----                -------         ------
student["name"]     Access name     "Aman"
student["age"]      Access age       21
student["course"]   Access course   "Python"

'''

# KeyError Example
person = {"name":"Rajesh","age":23,"type":"employee"}
print(person["name"]) # Rajesh
print(person["city"]) # KeyError: 'city'  The key "city" does not exist.
