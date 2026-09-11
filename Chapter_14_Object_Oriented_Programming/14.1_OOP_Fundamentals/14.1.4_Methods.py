""" 
A method is a function defined inside a class.

Synatx:
  class ClassName:
    def method_name(self):
      statement
  
1. Methods define object behavior.
2. Methods are functions inside a class.
3. Instance methods usually take self as the first parameter.
4. Methods are called using an object.
"""

class Student:
  def greet(self):
    print("Good Morning")
    
student1 = Student()
student1.greet()    # Good Morning