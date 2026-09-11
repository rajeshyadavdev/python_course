""" 
__repr__ returns a developer-friendly string representation of an object.

Synatx:
  def __repr__(self):
    return "Text"

1. __repr__ is called by repr(obj). It is mainly used for debugging.
2. It should return a string. A good __repr__ often looks like valid Python code.
3. If __str__ is not defined, Python may use __repr__ while printing.
    
"""
class Student:
  def __init__(self, name, course):
    self.name = name
    self.course = course

  def __repr__(self):
    return f"Student(name={self.name!r}, course={self.course!r})"

student = Student("Rajesh", "Python")
print(repr(student))
# Student(name='Rajesh', course='Python')
