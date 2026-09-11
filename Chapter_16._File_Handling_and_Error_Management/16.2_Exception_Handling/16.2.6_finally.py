""" 
The finally block always runs.

Syntax
try:
  risky_code
except ExceptionType:
  handling_code
finally:
  cleanup_code

Explanation
1. finally runs whether an exception occurs or not.
2. It is used for cleanup operations.
3. It is useful for closing files, network connections, or database connections.
4. With file handling, with is usually cleaner than manually using finally.
"""
try:
  file = open("data.txt", "r", encoding="utf-8")
  print(file.read())
except FileNotFoundError:
  print("File not found")
finally:
  print("Finally block executed")

''' 
Welcome to python coding
Finally block executed
'''