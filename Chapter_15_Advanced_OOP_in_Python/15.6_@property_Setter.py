""" 
A setter is used to control how a property value is updated.

Syntax
  @property
  def name(self):
    return self._name
    
  @name.setter
  def name(self, value):
    self._name = value

Explanation
1. A getter returns the value.
2. A setter updates the value.
3. The setter can validate the value before saving it.
4. This protects objects from invalid data.
5. The property name and setter name must match.
"""
class Student:
  def __init__(self, marks):
    self.marks = marks
  @property
  def marks(self):
    return self._marks
  @marks.setter
  def marks(self, value):
    if value < 0:
      raise ValueError("Marks cannot be negative")
    self._marks = value
    
student = Student(80)
student.marks = 95
print(student.marks) # 95

# Getter and Setter Table
''' 
Part              Purpose
====              =======
@property         Reads value
@marks.setter     Updates value
self._marks       Internal storage attribute
student.marks     Public property access
'''

