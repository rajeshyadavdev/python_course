""" 
Syntax:
  from collections import namedtuple
  TupleName = namedtuple("TupleName", ["field1", "field2"])
  object_name = TupleName(value1, value2)
  
Explanation
  1. A named tuple is a tuple with named fields.
  2. Normal tuple values are accessed by index.
  3. Named tuple values can be accessed by name.
  4. This makes code more readable.
  5. Named tuples are immutable like normal tuples.
"""

from collections import namedtuple

Student = namedtuple("student",["name","age","course"])

student1 = Student("Rajesh",12,"python")
print(f"name:{student1.name}")     # name:Rajesh
print(f"age:{student1.age}")       # age:12
print(f"course:{student1.course}") # course:python

''' 
Normal Tuple vs Named Tuple
---------------------------
Normal Tuple          Named Tuple
------------          -----------
Access by index       Access by name
student[0]            student.name
Less readable         More readable
Immutable             Immutable
'''
