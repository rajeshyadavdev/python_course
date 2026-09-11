""" 
map() applies a function to every item of an iterable.

Synatx:
  map(function, iterable)

Explanation
  1. map() takes a function and an iterable.
  2. It applies the function to each item.
  3. In Python 3, map() returns a map object, which is an iterator.
  4. To display all results at once, convert it using list().
  
"""

# Example 1
numbers = [1, 2, 3, 4]
square = map(lambda number :  number * number,  numbers)
print(square) # <map object at 0x00000227A4E35CC0>
print(list(square)) # [1, 4, 9, 16]


# Example 2
names = ["rajesh","rakesh","ramesh"]
upper_name = map(str.upper,names)
print(list(upper_name)) # ['RAJESH', 'RAKESH', 'RAMESH']

''' 
Part                              Meaning
====                              =======
lambda number: number * number    Function to apply
numbers                           Iterable
map()                             Applies function to every item
list()                            Converts result into a list
'''