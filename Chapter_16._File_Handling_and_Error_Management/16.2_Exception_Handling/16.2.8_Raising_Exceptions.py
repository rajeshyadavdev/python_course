""" 
Raising an exception means creating an error manually.

Syntax
  raise ExceptionType("message")
  
1. raise is used to manually trigger an exception.
2. It is useful for validation.
3. It stops normal flow and sends control to exception handling.
4. We can raise built-in or custom exceptions.

"""
age = -5
if age < 0:
  raise ValueError("Age cannot be negative")

# ValueError: Age cannot be negative