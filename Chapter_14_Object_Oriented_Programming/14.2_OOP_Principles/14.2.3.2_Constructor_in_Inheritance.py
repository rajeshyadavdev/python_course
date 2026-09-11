""" 
When a child object is created, Python runs the child class __init__ method.
If the child class does not have __init__, Python uses the parent class __init__.

"""
# Case 1: Child Has No __init__
class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):
  pass

student = Student("Aman")
print(student.name)
# Aman

# The child class uses the parent class constructor.


# Case 2: Child Has Its Own __init__
class Employee:
  def __init__(self, name):
    self.name = name

class Candidate(Employee):
  def __init__(self, course):
    self.course = course

candidate = Candidate("Python")
print(candidate.course)
# Python

# Here, parent __init__ does not run automatically because the child has its own __init__.
