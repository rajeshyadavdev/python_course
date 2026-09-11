""" 
__str__ returns a user-friendly string representation of an object.

Synatx:
  def __str__(self):
    print("Text")
    
Explanation
  1. __str__ is called by str(obj).
  2. It is also called by print(obj).
  3. It should return a string.
  4. It is mainly for users.
  5. It should be readable and simple.
"""
class Student:
  def __init__(self, name, course):
    self.name = name
    self.course = course

  def __str__(self):
    return f"{self.name} is studying {self.course}"


student = Student("Rajesh", "Python")
print(student)
# Rajesh is studying Python