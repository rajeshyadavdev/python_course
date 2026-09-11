""" 
The else block runs only when no exception occurs.

Syntax:
try:
  risky_code
except ExceptionType:
  handling_code
else:
  code_if_no_error
  
  
1. else runs only if the try block has no exception. It is useful for success logic.
2. It keeps error handling separate from normal code.  
"""
try:
  number = int("123")
except ValueError as error:
  print(error)
else:
  print("Conversion successful:", number)

# Conversion successful: 123