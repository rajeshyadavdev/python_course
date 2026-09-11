""" 
Syntax:
  iterator = iter(sequence)
  value = next(iterator)

Explanation
  1. An iterator is an object that gives values one by one.
  2. iter() creates an iterator from an iterable value.
  3. next() gets the next value from the iterator.
  4. Loops internally use this idea to get values one by one.

Term Meaning
------------
  Iterable Something that can be looped over
  Iterator Object that gives values one by one
  iter() Creates an iterator
  next() Gets the next value
  
  
FLOW-CHART
----------
Itertable value
  |
  iter() 
  |
  Iterator created  
  |
  next()
  |
  One value return
  |
  next()
  |
  Next value return
"""

# Example 1: Using iter() and next()
letter = "ABC"
iterator = iter(letter)
value_1 = next(iterator)
value_2 = next(iterator)
value_3 = next(iterator)
print(value_1,value_2,value_3) # A B C



# Iterable vs Iterator
''' 
Term          Meaning                                 Example
----          -------                                 -------
Iterable      Something we can loop over              String, range()

Iterator      Object that gives values one by one     Created using iter()

iter()        Creates an iterator                     iter("ABC")

next()        Gets next value                         next(iterator)
'''
