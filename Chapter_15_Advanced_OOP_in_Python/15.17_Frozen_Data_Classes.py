""" 
A frozen data class creates objects that cannot be modified after creation.

Synatx:
  @dataclass(frozen=True)
  class class_name:
    field_name = type
  
Explanation
1. frozen=True makes data class objects immutable-like.
2. After object creation, fields cannot be reassigned normally. It is useful for fixed data.
3. It is similar in idea to immutability, but internal mutable fields can still be modified if
they exist.
  
"""
from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
  x: int
  y: int
  
point = Point(10,20) 
print(point) 
# Point(x=10, y=20)
''' 
Invalid update:
point.x = 50
Output: dataclasses.FrozenInstanceError: cannot assign to field 'x'
'''