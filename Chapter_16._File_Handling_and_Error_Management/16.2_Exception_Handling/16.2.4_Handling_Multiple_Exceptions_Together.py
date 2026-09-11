""" 
Multiple exception types can be handled in one except block.

Syntax:
  except (ErrorType1, ErrorType2):
    statement
"""
# Example
try:
  value = int("abc")
except (ValueError, TypeError):
  print("Invalid conversion")
  
# Invalid conversion
  

