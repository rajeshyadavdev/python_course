""" 
Comparison methods allow objects to be compared.

Synatx:
  def __eq__(self,other):
    return result

Explanation
1. __eq__ defines equality using ==.
2. __lt__ defines less than using <.
3. Other comparison methods work similarly.
4. These methods should return True or False.
5. Return NotImplemented if comparison with the other type is unsupported.

"""
class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def __eq__(self, other):
    if not isinstance(other, Student):
      return NotImplemented
    return self.marks == other.marks

student1 = Student("Rajesh", 85)
student2 = Student("Riya", 85)
print(student1 == student2) # True

# Here, two students are considered equal because their marks are equal.

# Comparison Methods Table
''' 
Method    Operator
======    ========
__eq__    ==
__ne__    !=
__lt__    <
__le__    <=
__gt__    >
__ge__    >=
'''