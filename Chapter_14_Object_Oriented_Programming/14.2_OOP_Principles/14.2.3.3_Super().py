""" 
super() is used to call the next method in the MRO, usually from the parent class.

Syntax
  super().method_name()

Explanation
1. super() is commonly used to call parent class methods.
2. It is commonly used inside __init__.
3. It avoids directly writing the parent class name.
4. In multiple inheritance, super() follows MRO.
5. It helps avoid repeating parent class logic.
"""
class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):
  def __init__(self, name, course):
    super().__init__(name)
    self.course = course

student = Student("Aman", "Python")
print(student.name)
print(student.course)

# Aman
# Python