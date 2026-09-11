""" 
Multiple except blocks are used to handle different errors differently.

Syntax:
try:
  risky_code
except ErrorType1:
  handling_code
except ErrorType2:
  handling_code
  
Explanation
1. Different exceptions can need different handling.
2. Specific exceptions should come before general exceptions.
3. Python runs only the first matching except block.
4. Exception should usually come last.
  
"""
try:
  numbers = [10, 20, 30]
  print(numbers[5])
except IndexError:
  print("Invalid index")
except ValueError:
  print("Invalid value")
except Exception:
  print("Some other error occurred")
  
# Invalid index  