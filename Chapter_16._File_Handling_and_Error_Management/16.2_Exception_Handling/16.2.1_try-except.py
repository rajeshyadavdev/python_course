""" 
try-except is used to handle exceptions.
Syntax
  try:
    risky_code
  except ExceptionType:
    handling_code

1. Code that may cause an error is written inside try.
2. Error handling code is written inside except.
3. If an exception occurs, Python jumps to the matching except block.
4. If no exception occurs, the except block is skipped.

Flow Chart
==========
try block runs
|
v
Error occurs?
|
├── Yes -> except block runs
|
└── No -> except block skipped
"""
try:
  number = int("abc")
except ValueError:
  print("Invalide input")  
  
# Invalide input 