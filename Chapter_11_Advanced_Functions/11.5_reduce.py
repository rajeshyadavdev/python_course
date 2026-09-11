""" 
reduce() combines all items of an iterable into a single final value. 
reduce() is not directly available like map() and filter(). 
It must be imported from functools.

Syntax
  from functools import reduce
  reduce(function, iterable)

Explanation
  1. reduce() takes a function and an iterable.
  2. It combines values step by step.
  3. It returns one final result.
  4. It is useful for cumulative calculations.
  5. For simple addition, sum() is usually better.
"""

from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)

print(total) # 10

''' 
Working idea:
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
'''

# map() vs filter() vs reduce()
''' 
Function        Purpose                 Final Result
========        =======                 ============
map()           Transform items         Iterator of transformed items
filter()        Select items            Iterator of selected items
reduce()        Combine items           Sing
'''