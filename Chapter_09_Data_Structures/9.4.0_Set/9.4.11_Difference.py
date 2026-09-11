""" 
Syntax:
  set1 - set2
  set1.diffrence(set2)
  
1. Difference returns values present in the first set but not in the second set.
2. a - b and b - a can give different results.
  
"""
a = {1,2,3}
b = {3,4,5}

c = a-b
d = a.difference(b)
print(c) # {1, 2} 
print(d) # {1, 2} 

e = b-a
f = b.difference(a)
print(e) # {4, 5}
print(f) # {4, 5}


# a - b = values in a but not in b = {1, 2}
# b - a = values in b but not in a = {4, 5}

