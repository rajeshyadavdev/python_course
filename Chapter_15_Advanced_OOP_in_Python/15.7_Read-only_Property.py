""" 
A property becomes read-only if we define only getter and no setter.

Syntax
  @property
  def property_name(self):
    return value
Explanation
1. If no setter is defined, the property cannot be assigned directly.
2. This is useful for calculated values.
3. It protects values from direct modification.
"""
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  @property
  def area(self):
    return self.length * self.width

rectangle = Rectangle(10, 5)
print(rectangle.area) # 50

''' 
Invalid update:
rectangle.area = 100
Output:
AttributeError: property 'area' of 'Rectangle' object has no setter
'''
