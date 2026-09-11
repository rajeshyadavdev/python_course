""" 
A custom exception is a user-defined exception class.

Syntax
class CustomError(Exception):
  pass

Explanation
1. Custom exceptions are created by inheriting from Exception.
2. They make errors more meaningful.
3. They are useful in larger projects.
4. Custom exception names usually end with Error.

"""
class InsufficientBalanceError(Exception):
  pass
balance = 500
withdraw_amount = 1000
if withdraw_amount > balance:
  raise InsufficientBalanceError("Not enoughbalance")

# InsufficientBalanceError: Not enoughbalance