""" 
Syntax:
  first, *middle, last = tuple_name
  
Explanation
1. Extended unpacking is used when we do not want to manually create variables for
every value.
2. The starred variable collects extra values.
3. The starred variable becomes a list.

"""
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(f"first:{first}")   # first:10
print(f"middle:{middle}") # middle:[20, 30, 40]
print(f"last:{last}")     # last:50

# Important point: The starred variable stores values in a list, not a tuple.
