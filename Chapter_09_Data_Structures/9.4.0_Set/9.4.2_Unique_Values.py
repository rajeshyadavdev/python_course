""" 
Syntax:
  set_name = {value1, value2, value1}

1. Sets automatically remove duplicate values.
2. Each value appears only once.
3. This makes sets useful for removing duplicates from data.
4. Sets check uniqueness using the value, not position.
"""
numbers = {10, 20, 10, 30, 20, 40}
print(numbers) 
# Output: {40, 10, 20, 30} => Duplicate 10 and 20 are removed.



# Removing Duplicates from a List
numbers = [10, 20, 10, 30, 20, 40]
unique_numbers = set(numbers)
print(unique_numbers) # {40, 10, 20, 30}

