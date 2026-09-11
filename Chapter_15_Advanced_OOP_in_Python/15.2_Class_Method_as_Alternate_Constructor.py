""" 
An alternate constructor means creating an object in a different way.

Syntax

  @classmethod
  def method_name(cls,data):
    return cls(...)
    
1. A class normally creates objects using __init__.
2. Sometimes data comes in a different format.
3. A class method can convert that data and return an object.
4. cls(...) creates an object of the current class.
5. This is useful for flexible object creation.
    
"""
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def from_string(cls, data):
    name, age = data.split("-")
    return cls(name, int(age))

student = Student.from_string("Aman-21")
print(student.name)
print(student.age)
''' 
Aman
21
'''