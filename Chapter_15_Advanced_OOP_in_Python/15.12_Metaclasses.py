""" 
A metaclass is the class of a class.

Basic Idea
==========
Object is created from class. Class is created from metaclass.
1. In Python, classes are also objects.
2. The default metaclass in Python is type.
3. A metaclass controls how a class is created.
4. Metaclasses are advanced.
5. Most normal Python programs do not need custom metaclasses.
6. For Core Python, understanding the basic idea is enough.

"""

class Student:
  pass

student = Student()

print(type(student))
print(type(Student))

''' 
Output: 
<class '__main__.Student'>
<class 'type'>

Code Meaning
type(student) student is an object of Student
type(Student) Student is an object of type
'''