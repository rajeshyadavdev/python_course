""" 
JSON means JavaScript Object Notation. JSON is commonly used for APIs and
configuration files.

Example of JSON Data
====================
{
"name": "Aman",
"age": 21,
"course": "Python"
}


Explanation
1. JSON stores data in key-value format. It looks similar to Python dictionaries.
2. Python provides the built-in json module.
3. JSON is very common in web development and APIs. JSON keys must be strings.

Python and JSON Conversion
==========================
Python       JSON
dict         object
list         array
str          string
int, float   number
True         true
False        false
None         null
"""
# Reading JSON File
import json

with open("student.json", "r",encoding="utf-8") as file:
  data = json.load(file)
  print(data["name"])
  


# Writing JSON File
student = {
"name": "Rajesh",
"age": 21,
"course": "Python"
}
with open("student.json", "w", encoding="utf-8") as file:
  json.dump(student, file, indent=4)
 