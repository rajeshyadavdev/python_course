""" 
Syntax
  set1.issubset(set2)
  set1.issuperset(set2)
  set1.isdisjoint(set2)

1. A subset means all values of one set exist inside another set.
2. A superset means one set contains all values of another set.
3. Disjoint sets have no common values.
"""
a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}
print(a.issubset(b))   # True
print(b.issuperset(a)) # True
print(a.isdisjoint(c)) # True

''' 
Comparison Table
================

Concept     Meaning                     Example                       Result
-------     -------                     -------                       ------
Subset      All items of a are in b     {1, 2} <= {1, 2, 3}           True
Superset    b contains all items of a   {1, 2, 3} >= {1, 2}           True
Disjoint    No common items             {1, 2}.isdisjoint({3, 4})     True
'''