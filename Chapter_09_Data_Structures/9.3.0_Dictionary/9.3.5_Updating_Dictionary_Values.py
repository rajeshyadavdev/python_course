""" 
Syntax:
  dictionary_name[key] = new_value

Explanation
  1. Dictionaries are mutable.
  2. Existing values can be updated using keys.
  3. If the key already exists, its value is updated.
  4. If the key does not exist, a new key-value pair is added.
   
"""
student = {
"name": "Aman",
"age": 21
}
student["age"] = 22
student["course"] = "Python"
print(student)
# {'name': 'Aman', 'age': 22, 'course': 'Python'}

