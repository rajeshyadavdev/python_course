""" 
Syntax:
for key in dictionary:
  statement
  

for key, value in dictionary.items():
  statement
  
Explanation
  1. A dictionary can be looped through using for.
  2. By default, looping over a dictionary gives keys.
  3. Use values() to loop through values.
  4. Use items() to loop through both keys and values.
    
"""
student = {
"name": "Aman",
"age": 21,
"course": "Python"
}
for key, value in student.items():
  print(key, value)
  
''' 
name Aman
age 21
course Python
'''  
