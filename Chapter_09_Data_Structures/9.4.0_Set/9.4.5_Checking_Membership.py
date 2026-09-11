""" 
Syntax:
value in set_name
value not in set_name

Explanation
  1. Sets are very useful for checking whether a value exists.
  2. in returns True if value exists.
  3. not in returns True if value does not exist.
  4. Membership checking in sets is usually faster than lists for large data.

"""

numbers = {10,20,30,40,50}
print(10 in numbers) # True
print(80 in numbers) # False

print(10 not in numbers) # False
print(80 not in numbers) # True

