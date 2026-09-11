""" 
Syntax:
  dictionary = {"key":"value"}
  
Explanation
  1. A key is used to identify a value.
  2. A value is the data stored against the key.
  3. Keys must be unique.
  4. Values can be duplicate.
  5. Keys should be immutable types like string, number, or tuple.
    
"""
student = {"name":"Rajesh","age":21,"course":"Python"}
print(student["name"]) # Rajesh


# Key Rules Table
''' 
Rule            Allowed?                Example
----            -------                 -------
String key      Yes                   "name": "Aman"
Number key      Yes                   1: "One"
Tuple key       Yes                   (10, 20): "Point"
List key        No                    [1, 2]: "Value"
Duplicate keys  Not useful            Last value is kept
'''

# Duplicate Key Example
student = {
  "name":"Rajesh",
  "name":"Ramesh"
  }
print(student) # {'name': 'Ramesh'}

# The second value replaces the first value because dictionary keys must be unique.