""" 
A data class is a class mainly used to store data. It reduces repeated code like __init__,
__repr__, and comparison methods.


from dataclasses import dataclass
  @dataclass
  class ClassName:
    field_name: type


Explanation
1. Data classes are created using @dataclass.
2. They are useful for classes that mainly store data.
3. Fields are declared using type annotations.
4. Python automatically creates __init__.
5. Python automatically creates useful __repr__.
6. Data classes were introduced in Python 3.7.    
"""
from dataclasses import dataclass
@dataclass
class Student:
  name: str
  age: int
  course: str

student = Student("Aman", 21, "Python")
print(student)
# Student(name='Aman', age=21, course='Python')

