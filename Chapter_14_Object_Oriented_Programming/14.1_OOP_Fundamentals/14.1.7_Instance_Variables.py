""" 
Instance variables are variables that belong to a specific object.

Syntax
    self.variable_name = value

1. Instance variables are usually created inside __init__.
2. Each object gets its own copy.
3. Changing one object’s instance variable does not affect another object.
4. They are accessed using object.variable_name.

"""
class Student:
    def __init__(self, name):
        self.name = name
        
student1 = Student("Rajesh")
student2 = Student("Riya")
print(student1.name)  # Rajesh
print(student2.name)  # Riya

# NOTE: student1.name and student2.name are separate instance variables.
  