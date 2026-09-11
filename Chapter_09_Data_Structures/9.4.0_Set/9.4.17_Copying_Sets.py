""" 
Syntax:
  new_set = old_set.copy()

1. copy() creates a shallow copy of a set. Direct assignment does not create a new set.
2. Direct assignment makes both variables point to the same set.

"""
a = {10, 20, 30}
b = a.copy()
b.add(40)
print(a) # {10, 20, 30}
print(b) # {40, 10, 20, 30}


# Copying Table
''' 
Code              Creates New Set?                  Meaning
b = a             No                                Same set reference
b = a.copy()      Yes                               Shallow copy
b = set(a)        Yes                               New set

'''
