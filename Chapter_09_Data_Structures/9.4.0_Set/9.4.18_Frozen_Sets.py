""" 
A frozenset is an immutable version of a set.

Syntax:
  frozenset_name = frozenset(iterable)
  
  
1. A normal set is mutable. A frozenset is immutable.
2. Values cannot be added or removed from a frozenset. Frozensets can be used as
  dictionary keys or set elements.
3. Frozensets support read-only set operations like union, intersection, and difference.

"""

numbers = frozenset([10, 20, 30])
print(numbers)
print(type(numbers))

# frozenset({10, 20, 30})
# <class 'frozenset'>


# Invalid Operation
numbers = frozenset([10, 20, 30])

numbers.add(40) # AttributeError: 'frozenset' object has no attribute 'add'



# Set vs Frozen Set Table
''' 
Point                     Set               Frozenset
-----                     ---               ---------
Mutable                   Yes               No
Add items                 Allowed           Not allowed
Remove items              Allowed           Not allowed
Unique values             Yes               Yes
Unordered                 Yes               Yes
Can be dictionary key     No                Yes
Can be set element        No                Yes
Syntax                    {1, 2, 3}         frozenset([1, 2, 3])
'''

# Frozenset Methods Table
''' 
Method                      Available in Frozenset?     Reason
union()                     Yes                         Does not modify original
intersection() Yes Does not modify original
difference() Yes Does not modify original
symmetric_difference() Yes Does not modify original
issubset() Yes Only checks
issuperset() Yes Only checks
isdisjoint() Yes Only checks
add() No Modifies set
remove() No Modifies set
discard() No Modifies set
clear() No Modifies set
update() No Modifies set
'''
