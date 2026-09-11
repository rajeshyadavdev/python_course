""" 
Syntax
  set1.intersection_update(set2)
  set1.difference_update(set2)
  set1.symmetric_difference_update(set2)

1. Normal set operation methods return a new set.
2. Update methods change the original set.
3. These are useful when we do not need the old s
"""
#   set1.intersection_update(set2)
set1 = {10,20,30}
set2 = {30,40,50}

set1.intersection_update(set2)
print(set1) # {30}
