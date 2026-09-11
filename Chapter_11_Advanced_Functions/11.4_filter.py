""" 
filter() is used to select items from an iterable based on a condition.

Syntax
  filter(function, iterable)

Explanation
  1. filter() takes a function and an iterable.
  2. The function must return True or False.
  3. Items that return True are kept.
  4. Items that return False are removed.
  5. In Python 3, filter() returns a filter object, which is an iterator.



Flow Chart
==========
Iterable values
|
v
filter() checks condition
|
├── True -> keep item
|
└── False -> remove item
|
v
Filtered result
"""

numbers = [1, 2, 3, 4, 5, 6]
even_number = filter(lambda number : number %2 == 0,numbers)
print(even_number) # <filter object at 0x0000016923C35DE0>
print(list(even_number)) # [2, 4, 6]


# map() vs filter()
''' 
Point               map()                       filter()
Purpose             Transforms every item       Selects matching items
Output length       Usually same as input       Can be smaller
Function returns    New value                   True or False
Example use         Square every number         Keep even numbers
'''