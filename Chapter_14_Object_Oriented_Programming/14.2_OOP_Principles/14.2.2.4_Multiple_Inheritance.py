""" 
Multiple inheritance means one child class inherits from more than one parent class.

Syntax:
  class Parent1:
    pass
  
  class Parent2:
    pass
    
  class child(Parent1,Parent2):
    pass  


1. Python supports multiple inheritance.
2. A child class can use methods from multiple parent classes.
3. If parents have methods with the same name, Python uses MRO.
4. MRO means Method Resolution Order.
"""
class Father:
  def __init__(self):
    pass
  def father_skill(self):
    print("Gardening")  
    
class Mother:
  def __init__(self):
    pass
  def mother_skill(self):
    print("Cooking")   
    
class Child(Father,Mother):
  def __init__(self):
    pass
  def child_skill(self):
    print("Coding")  
    
child = Child()   
child.father_skill()
child.mother_skill()
child.child_skill()    
''' 
Gardening
Cooking
Coding
'''