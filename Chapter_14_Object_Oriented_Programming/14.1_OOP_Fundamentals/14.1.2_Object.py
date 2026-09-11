""" 
An object is an instance created from a class.

Syntax
======
  object_name = ClassName()

1. An object is created from a class.
2. One class can create many objects.
3. Each object can have its own data.
4. Objects are also called instances.

"""
class Student:
  pass

student1 = Student()
student2 = Student()
print(student1)
print(student2)
# <__main__.Student object at 0x000002043D7D5D60>
# <__main__.Student object at 0x000002043D7D5CD0>

# The memory address may be different in every run.


# Class vs Object
''' 
Point                  Class                Object
=====                 ======                ======
Meaning               Blueprint             Real instance
Created using         class keyword         Class name with ()
Example               Student               student1 = Student()
Memory                No object data yet    Stores actual object data.
'''