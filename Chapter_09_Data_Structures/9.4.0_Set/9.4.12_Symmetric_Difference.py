""" 
Synatx:
  set1 ^ set2
  set1.symmetric_difference(set2)

1. Symmetric difference returns values that are not common.
2. It removes common values from the final result.

"""
a = {1,2,3}
b = {3,4,5}

c = a ^ b
d = a.symmetric_difference(b)
print(c) # {1, 2, 4, 5}
print(d) # {1, 2, 4, 5}

