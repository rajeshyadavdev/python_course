""" 
Syntax:
value_if_true if condition else value_if_false

common usage
------------
variable = value_if_true if condition else value_if_false


The ternary operator is a short way to write a simple if-else statement in one line. It is useful
when we need to choose between two values. Use it only for simple conditions. For complex
logic, normal if-else is better.

FLOW_CHART
----------
Start
|
|---> True --> return value_if_true
|
|---> False --> return value_if_false
|
|
Store/use result

"""

# Normal if-else:

age = 27
if age >= 18:
  status = "Adult"
else:
  status = "Minor" 
print(status)

# Adult


# Same code using ternary operator:
status = "Adult" if age >= 18 else "Minor"
print(status) # Adult



