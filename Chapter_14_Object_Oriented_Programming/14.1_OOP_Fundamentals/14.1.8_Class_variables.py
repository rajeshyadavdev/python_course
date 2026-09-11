""" 
Class variables are variables shared by all objects of a class.

Syntax:
  class ClassName:
    class_variable = value
    
Explanation
1. Class variables are defined directly inside the class.
2. They are shared by all objects.
3. They are useful for common data.
4. They can be accessed using the class name or object name.
5. Prefer accessing class variables using the class name.    
"""

class Student:
  school_name = "ABC School"
  def __init__(self, name):
    self.name = name

student1 = Student("Rajesh")
student2 = Student("Riya")

print(student1.school_name)   #ABC School
print(student2.school_name)   #ABC School
print(Student.school_name)    #ABC School



# Instance Variable vs Class Variable
''' 
Point                   Instance Variable                 Class Variable
=====                   =================                 ==============
Belongs to              Object                            Class
Created where           Usually inside __init__           Inside class, outside methods
Shared?                 No                                Yes
Access                  self.name                         ClassName.variable
Example                 self.name                         school_name
'''

# Important Warning
# Avoid mutable class variables unless shared data is intentional.

class Student:
  subject = []
  
# This list is shared by all objects, which can cause unexpected behavior.
