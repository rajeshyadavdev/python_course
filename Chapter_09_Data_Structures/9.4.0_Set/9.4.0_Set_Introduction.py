""" 
A set is a data structure used to store multiple unique values.

Syntax:
  set_name = {value_1,value_2,value_3}
  
  
Explanation
  1. Sets are written using curly braces {}.
  2. Set items are separated by commas.
  3. Sets store only unique values.
  4. Sets are unordered, so items do not have fixed positions.
  5. Sets are mutable, so we can add or remove items.
  6. Set elements must be immutable/hashable values.
  
"""
numbers = {10, 20, 30, 40}
print(numbers)
# {40, 10, 20, 30} : The output order may look different because sets are unordered.


# Set Properties Table
''' 
Property               Meaning                                 Example
--------               -------                                 -------
Unordered              Items have no fixed index               Cannot use items[0]

Unique values          Duplicate values are removed            {10, 10, 20} becomes {10, 20}

Mutable                Items can be added/removed              items.add(50)

Unindexed              No indexing/slicing                     items[1] not allowed

Mixed data allowed     Can store different immutable types     {10, "Aman", True}

Fast membership check  Good for checking existence             10 in numbers
'''


