""" 
Syntax:
  tuple_name = (value,)

Explanation
  1. A single-item tuple must contain a comma.
  2. Without the comma, Python does not treat it as a tuple.
  3. Parentheses alone are not enough.

"""
# Example1
tuple_1 = ("Python")
tuple_2 = ("Python",)
print(type(tuple_1))  # <class 'str'>
print(type(tuple_2))  # <class 'tuple'>

