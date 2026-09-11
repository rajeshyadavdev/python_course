""" 
Explanation
This concept matters when a list contains another list. There are two types of copy:
  ● Shallow copy
  ● Deep copy
  
"""
# Shallow copy
# A shallow copy creates a new outer list, but nested lists inside are still shared.
list1 = [[10, 20], [30, 40]]
list2 = list1.copy()

list2[0][0] = 100
print(list1) #[[100, 20], [30, 40]]
print(list2) #[[100, 20], [30, 40]]
''' 
1. list1.copy() creates a new outer list.
2. But the inner lists are still shared.
3. So changing an inner list affects both lists.
'''

# Deep Copy
# A deep copy creates a completely separate copy of both the outer list and inner lists.
import copy
list1 = [[10, 20], [30, 40]]

list2 = copy.deepcopy(list1)

list2[0][0] = 100
print(list1) # [[10, 20], [30, 40]]
print(list2) # [[100, 20], [30, 40]]

''' 
Explanation
1. copy.deepcopy() creates a fully independent copy.
2. Inner lists are also copied separately.
3. Changing list2 does not affect list1.

'''


# Shallow Copy vs Deep Copy Table
''' 
Point                             Shallow Copy                  Deep Copy
-----                             -----------                   ---------
1. Outer list                     New copy                      New copy

2. Inner                          nested lists                  Shared New copy

3. Affects original nested data?  Yes                           No

4. Common method                  copy()                        copy.deepcopy()

5. Useful for                     Simple lists                  Nested lists
'''
