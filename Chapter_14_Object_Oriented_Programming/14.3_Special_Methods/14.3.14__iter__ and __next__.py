""" 
These methods make an object iterable.

Syntax:
  def __iter__(self):
    return self
  
  def __next__(self):
    return next_value

1. __iter__ returns an iterator object. __next__ returns the next value.
2. When no value is left, __next__ should raise StopIteration.
3. These methods are used by loops. They are part of the iterator protocol.

"""
class CountUpTo:
  def __init__(self, limit):
    self.current = 1
    self.limit = limit

  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.limit:
      raise StopIteration
    value = self.current
    self.current += 1
    return value
  
counter = CountUpTo(3)
for number in counter:
  print(number)
  
''' 
1
2
3
'''
  