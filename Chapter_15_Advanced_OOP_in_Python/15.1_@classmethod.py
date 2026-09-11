""" 
A class method is a method that receives the class as its first argument.
The first parameter is usually named cls.

Syntax
  class ClassName:
    @classmethod
    def method_name(cls):
      statement

Explanation
  1. @classmethod is used to create a class method.
  2. A class method receives the class automatically as cls.
  3. It can access class variables.
  4. It can modify class variables.
  5. It can be called using the class name or object name.
  6. It is commonly used to create alternate constructors.
"""
class Student:
  school_name = "ABC School"

  def __init__(self, name):
    self.name = name
  @classmethod
  def change_school(cls, new_school):
    cls.school_name = new_school

Student.change_school("XYZ School")
student1 = Student("Aman")
print(student1.school_name)
print(Student.school_name)

''' 
XYZ School
XYZ School
'''

# Important Points
''' 
Point                                     Explanation
=====                                     ===========
First parameter                           cls

Receives                                  Class

Can access class variables                Yes

Can access instance variables directly    No

Can be called by class                    Yes

Can be called by object                   Yes
'''
