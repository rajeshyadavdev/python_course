""" 
We can store the exception object using as.

Syntax
  except ExceptionType as error:
    statement

"""
try:
  number = int("abc")
except ValueError as error:
  print(error)

# invalid literal for int() with base 10: 'abc'