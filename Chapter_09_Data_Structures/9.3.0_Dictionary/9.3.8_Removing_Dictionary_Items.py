""" 
Syntax
  dictionary.pop(key)
  dictionary.popitem()
  del dictionary[key]
  dictionary.clear()

Explanation
  1. pop(key) removes a specific key and returns its value.
  2. popitem() removes the last inserted key-value pair.
  3. del removes a specific key.
  4. clear() removes all items
"""

# Removing Items Table
''' 
Method / Keyword       Purpose                    Example
----------------       -------                    -------
pop(key)               Removes specific key       student.pop("age")
popitem()              Removes last pair          student.popitem()
del                    Deletes specific key del   student["age"]
clear()                Empties dictionary         student.clear()

'''
student = {
"name": "Aman",
"age": 21,
"course": "Python"
}
student.pop("age")
print(student) # {'name': 'Aman', 'course': 'Python'}

