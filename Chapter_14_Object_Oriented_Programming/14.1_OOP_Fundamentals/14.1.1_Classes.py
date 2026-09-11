""" 
A class is a blueprint for creating objects.

Synatx:
    class ClassName:
        statement

1. A class defines the structure of an object.
2. A class can contain attributes and methods.
3. Class names usually use PascalCase.
4. A class does not represent one real object by itself.
5. Objects are created from classes.
"""
class Student:
    pass
student1 = Student()
print(type(student1)) # <class '__main__.Student'>

# Class Naming Style
''' 
Good Class Name             Reason
---------------             ------
Student                     Clear class name
BankAccount                 Uses PascalCase
EmployeeRecord              Meaningful name
'''