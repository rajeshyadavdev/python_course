""" 
Re-raising means raising the same exception again after catching it.

Syntax
  raise

1. Plain raise is used inside an except block.
2. It re-raises the current exception.
3. It is useful when we want to log an error but still allow it to continue upward.

"""
try:
  number = int("abc")
except ValueError:
  print("Logging error")
  raise  

# Logging error
# ValueError: invalid literal for int() with base 10: 'abc'