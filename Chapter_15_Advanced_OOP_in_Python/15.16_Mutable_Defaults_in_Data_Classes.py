""" 
Do not directly use mutable default values like lists in data classes.

Wrong Style
===========
from dataclasses import dataclass

@dataclass
class Student:
  name:str
  subject:list = []
  
This is not allowed in modern Python data classes.
  
"""
# Correct Style : Use field(default_factory=list).

from dataclasses import dataclass,field
@dataclass
class Student:
  name:str
  subject:list = field(default_factory=list)
  
student1 = Student("Rajesh")  
student2 = Student("Riya")  

student1.subject.append("Python")
print(student1.subject)
print(student2.subject)

''' 
['Python']
[]


1. Mutable defaults can accidentally be shared.
2. default_factory=list creates a new list for each object.
3. This avoids shared mutable data problems.
'''