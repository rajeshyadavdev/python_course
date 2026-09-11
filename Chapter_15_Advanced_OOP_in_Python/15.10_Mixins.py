""" 
A mixin is a small class that provides extra reusable behavior to another class.

Syntax
  class MixinName:
    def method_name(self):
      statement

  class MainClass(MixinName):
    pass
    
1. A mixin is used to add extra features.
2. A mixin is usually not meant to be used alone.
3. Mixins are commonly used with multiple inheritance.
4. A mixin should be small and focused.
5. Mixin class names often end with Mixin.
"""
class JsonMixin:
  def to_json(self):
    return self.__dict__

class Student(JsonMixin):
  def __init__(self, name, age):
    self.name = name
    self.age = age

student = Student("Aman", 21)
print(student.to_json())
# {'name': 'Aman', 'age': 21}

# Important Points
''' 
Point                 Explanation
=====                 ===========
Purpose               Add reusable behavior
Usually used alone?   No
Common with           Multiple inheritance
Naming style          Ends with Mixin
Best design           Small and focused
'''