""" 
A dictionary is a data structure used to store data in key-value pairs.
Syntax:
  1. A dictionary stores data using keys and values.
  2. Each key is connected to one value.
  3. Keys are used to access values.
  4. Dictionaries are mutable, so values can be changed.
  5. Dictionary keys must be unique.
  6. Dictionaries are written using curly braces {}.

"""
student = {"name":"Rajesh Yadav","age":21,"course":"Python"}
print(student) # {'name': 'Rajesh Yadav', 'age': 21, 'course': 'Python'}


# Dictionary Properties Table
''' 
Property                Meaning                            Example
--------                -------                            -------
Key-value               based Stores data as pairs         "name": "Aman"
Mutable                 Can be changed                     student["age"] = 22
Ordered                 Keeps insertion order              Python 3.7+
Unique keys             Duplicate keys are not allowed     Last value replaces old value
Fast lookup             Values are accessed using keys     student["name"]
Mixed values allowed    Values can be any data type        string, int, list, tuple, dict
'''
