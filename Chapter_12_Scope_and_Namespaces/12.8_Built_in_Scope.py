""" 
Built-in scope contains names already provided by Python.
Examples: print, len, type, range, sum, max, min

Explanation:
1. Built-in names are available automatically.
2. We do not need to define them.
3. Python searches built-in scope last in the LEGB rule.
4. Avoid using built-in names as variable names.

"""


numbers = [1,2,3,4]
print(len(numbers)) # 4

# Bad Practice
list = [1,2,3,4]

# This is bad because the list is already a built-in name. Do not use names like list, dict, str, int, sum, or max as variable names.

