""" 
Synatx:
  set1 & set2
  set1.intersection(set2)

1. Intersection returns only common values.
2. Values must exist in both sets.

"""
a = {1,2,3}
b = {3,4,5}

c = a.intersection(b)
d = a & b
print(c) # {3}
print(d) # {3}

