""" 
A tuple is a data structure used to store multiple values in one variable.

Tuples are similar to lists, but the main difference is:
List -> mutable -> can be changed
Tuple -> immutable -> cannot be changed

Syntax
  tuple_name = (value1, value2, value3)

Explanation
  1. Tuples are written using parentheses ().
  2. Tuple items are separated by commas.
  3. Tuples are ordered, so items have index positions.
  4. Tuples are immutable, so items cannot be changed after creation.
  5. Tuples allow duplicate values.
  6. Tuples can store different data types
"""
my_tuple = (1,"Rajesh",20.5,True)
print(my_tuple) # (1, 'Rajesh', 20.5, True)

''' 
Tuple Properties Table
----------------------
Property                Meaning                               Example
--------                -------                               -------
1.Ordered               Items have fixed positions            items[0]

2.Immutable             Items cannot be changed               items[1] = 50 not allowed

3.Allows duplicates     Same value can appear more than once  (10, 10, 20)

4.Mixed data allowed    Can store different data types        ("Aman", 20, True)

5.Indexed               Every item has position number        0, 1, 2...
'''