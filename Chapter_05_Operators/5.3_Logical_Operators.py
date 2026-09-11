""" 
Logical operators are used to combine Boolean values.
Python has three logical operators:
● and
● or
● not

These operators work with True and False.


and   => True when both sides are True
or    => True when at least one side is True
not   => Reverses True/False
"""

# and Operator
# The and operator gives True only when both values are True.
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

''' 
Truth table:
-----------
Left Value   Right Value  Result
  True          True      True
  True          False     False
  False         True      False
  False         False     False
'''
# Simple meaning: and means both conditions must be True.
age_valide = True
id_available = True

print(age_valide and id_available)  # True



# or Operator
# The or operator gives True when at least one value is True.
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

''' 
Truth table:
-----------
Left Value    Right Value     Result
True          True            True
True          False           True
False         True            True
False         False           False

or means at least one value must be True.
'''
has_phone = True
has_email = False
print(has_phone or has_email) #True



# not Operator
# The not operator reverses a Boolean value.
print(not True)   # False
print(not False)  # True


is_logged_in = True
print(not is_logged_in) # False


# Logical Operators with Comparisons
# Comparison operators return Boolean values. So they can be used with logical operators.

age = 20
marks = 85
print(age > 18 and marks > 80)  # True

''' 
Explanation: age > 18 True
marks > 80 True

True and True = True
'''
