""" 
Synatx
  set(iterable)
  list(set_name)
  tuple(set_name)
  
1. set() converts an iterable into a set.
2. This is often used to remove duplicates.
3. A set can be converted back to a list or tuple.
4. Order may change after converting to a set.

"""
numbers = [10, 20, 10, 30, 20]
unique_numbers = set(numbers)

print(unique_numbers) # {10, 20, 30}

print(list(unique_numbers)) # [10, 20, 30]

''' 
Conversion Table
================
Conversion            Code                      Result Type
----------            ----                      -----------
List to set           set([1, 2, 2])            Set
Tuple to set          set((1, 2, 2))            Set
String to set         set("banana")             Set of unique
Set to list           list({1, 2, 3})           List
Set to tuple          tuple({1, 2, 3})          Tuple
'''   