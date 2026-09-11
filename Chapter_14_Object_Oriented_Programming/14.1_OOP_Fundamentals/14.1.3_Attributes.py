""" 
Attributes are variables that belong to an object or class.

Syntax
    object_name.attribute_name = value

Explanation
1. Attributes store data about an object.
2. Each object can have different attribute values.
3. Attributes are accessed using dot . notation.
"""
class Student:
    pass
student1 = Student()
student1.name = "Aman"
student1.age = 21
print(student1.name)
print(student1.age)

# Aman
# 21

# Attribute Table
''' 
Code                        Meaning
====                        =======
student1.name               Accesses name attribute
student1.age                Accesses age attribute
student1.name = "Aman"      Creates/updates attribute
'''