""" 
__init__ is a special method used to initialize object data.

Synatx:
  class ClassName:
    def __init__(self):
      statement
  
1. __init__ runs automatically when an object is created.
2. It is used to set initial attribute values.
3. It is commonly called a constructor.
4. Technically, __init__ initializes the object after it is created.
5. The actual object creation is handled by __new__, which is advanced and usually not
   needed in core notes.  
"""

class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
student = Student("Rajesh",23)

print(student.name)   # Rajesh 
print(student.age)    # 23