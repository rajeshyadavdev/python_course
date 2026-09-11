""" 
A static method is a method inside a class that does not receive self or cls.

Syntax
  class ClassName:
    @staticmethod
    def method_name():
      statement

1. @staticmethod creates a static method.
2. It does not receive the object as self.
3. It does not receive the class as cls.
4. It behaves like a normal function placed inside a class.
5. It is used when the method is logically related to the class but does not need object
    or class data.
"""
class MathHelper:
  @staticmethod
  def add(a, b):
    return a + b
  
print(MathHelper.add(10,20)) #30

# Important Points
''' 
Point                                         Explanation
=====                                         ===========
First parameter                               No automatic first parameter
Receives object?                              No
Receives class?                               No
Can access instance variables directly?       No
Can access class variables directly?          No
'''