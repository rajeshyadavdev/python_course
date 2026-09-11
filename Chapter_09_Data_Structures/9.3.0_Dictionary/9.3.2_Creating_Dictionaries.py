""" 
Syntax:

dictionary_name = {
  "key1":"value1",
  "key2":"value2"
}


Explanation
  1. Dictionaries are created using {}.
  2. Keys and values are separated using a colon :.
  3. Each pair is separated using a comma.
  4. Keys are usually strings, but numbers and tuples can also be used.
  5. Values can be any data type.
  
"""

student = {
"name": "Rahul",
"age": 20,
"marks": 85.5,
"is_passed": True
}
print(student)
# {'name': 'Rahul', 'age': 20, 'marks': 85.5, 'is_passed': True}



# Different Ways to Create Dictionaries
# Empty dictionary 
data = {}
print(data) # {}

# Normal dictionary 
student = {"name": "Aman", "age": 21}
print(student) # {'name': 'Aman', 'age': 21}

# Using dict() 
student = dict(name="Aman", age=21)
print(student) # {'name': 'Aman', 'age': 21}


# Nested dictionary 
students = {"s1": {"name": "Aman"}}
print(students) # {'s1': {'name': 'Aman'}}


# Dictionary with list value 
data = {"marks": [80, 90, 85]}
print(data) # {'marks': [80, 90, 85]}

# Dictionary with tuple key 
points = {(10, 20): "A"}
print(points) # {(10, 20): 'A'}

