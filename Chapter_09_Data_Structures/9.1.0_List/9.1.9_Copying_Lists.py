""" 
Syntax:
  new_list = old_list.copy()

Other ways:
  1. new_list = old_list[:]
  2. new_list = list(old_list)
  

Explanation
  1. Copying means creating another list with the same values.
  2. Direct assignment does not create a real copy.
  3. Direct assignment makes two variables point to the same list.
  4. To create a separate list, use copy(), slicing, or list().  
"""
# Direct Assignment
list1 = [10, 20, 30]
list2 = list1
list2[1] = 100
print(list1) # [10, 100, 30]
print(list2) # [10, 100, 30]

''' 
Explanation:
  1. list2 = list1 does not create a new list.
  2. Both variables refer to the same list.
  3. So changing list2 also affects list1.
'''
print(id(list1)) # 2613951731968
print(id(list2)) # 2613951731968



# 1. copy(),  new = old.copy(), Creates shallow copy
list1 = [1,2,3]
list2 = list1.copy()

list2[1] = 100

print(list1) # [1, 2, 3]
print(list2) # [1, 100, 3]



# 2. Slicing,  new = old[:],  Creates shallow copy
old_list = [1,2,3,4]
new_list = old_list[:]

new_list[2] = 30
print("old list:",old_list) # old list: [1, 2, 3, 4]
print("new list:",new_list) # new list: [1, 2, 30, 4]

print(id(old_list)) # 1441292097792
print(id(new_list)) # 1441292384192


'''' 
Copying Methods Table
---------------------
Method                 Code                  Meaning
------                 ----                  -------
1. copy()              new = old.copy()      Creates shallow copy
2. Slicing             new = old[:]          Creates shallow copy
3. list()              new = list(old)       Creates shallow copy
4. Direct assignment   new = old             Not a real copy

'''
