""" 
@property allows a method to be accessed like an attribute.

Syntax
  class ClassName:
    @property
    def attribute_name(self):
      return value

Explanation
1. @property is used to create managed attributes.
2. It allows method logic to run when accessing an attribute.
3. It helps with encapsulation.
4. It can be used for validation.
5. It makes code cleaner than normal getter methods.
"""

class Student:
  def __init__(self, marks):
    self._marks = marks
  @property
  def marks(self):
    return self._marks

student = Student(85)
print(student.marks) # 85
''' 
Important point:
student.marks looks like an attribute, but internally it calls the marks() method.

'''