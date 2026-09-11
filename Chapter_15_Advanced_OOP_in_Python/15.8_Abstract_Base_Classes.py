""" 
An abstract base class defines a common structure that child classes must follow.

Syntax
  from abc import ABC, abstractmethod
  
  class ClassName(ABC):
    
    @abstractmethod
    def method_name(self):
      pass
      
1. Abstract base classes are created using ABC.
2. Abstract methods are created using @abstractmethod.
3. A class with abstract methods cannot be instantiated directly.
4. Child classes must implement all abstract methods.
5. Abstract base classes are useful when many classes should follow the same structure.

Abstract class
|
v
Defines required method
|
v
Child class must implement method
|
v
Child object can be       
"""
from abc import ABC, abstractmethod
class Shape(ABC):
  @abstractmethod
  def area(self):
    pass
  
class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side * self.side

square = Square(5)
print(square.area()) # 25

