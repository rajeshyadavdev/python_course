""" 
Synatx:
  set1 | set2
  set1.union(set2)


Explanation
  1. Union combines two sets.
  2. It returns all unique values from both sets.
  3. Duplicate/common values appear only once.

"""

a = {1,2,3}
b = {3,4,5}

c = a.union(b)
d = a | b
print(c) # {1, 2, 3, 4, 5}
print(d) # {1, 2, 3, 4, 5}

# Union = all unique values = {1, 2, 3, 4, 5}