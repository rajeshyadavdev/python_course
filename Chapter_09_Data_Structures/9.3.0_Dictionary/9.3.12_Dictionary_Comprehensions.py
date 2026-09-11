""" 
Synatx:
  new_dict = {key_expression: value_expression for item in sequence}
  
  with condition
  --------------
  new_dict = {key_expression: value_expression for item in sequence if condition}
  
  
Explanation
  1. Dictionary comprehension is a short way to create a dictionary.
  2. It is similar to list comprehension.
  3. It creates key-value pairs using a loop.
  4. It can also include conditions.  
"""

numbers = [1, 2, 3, 4]
squares = {number: number * number for number in numbers}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16}

# with condition
numbers = [1, 2, 3, 4,5,6]

even_squares = {number: number * number for number in numbers if number % 2 == 0}
print(even_squares) # {2: 4, 4: 16, 6: 36}

''' 
Dictionary Comprehension Parts
------------------------------
Part                            Meaning
----                            -------
number                          before : Key
number * number                 Value
for number in numbers           Loop
if number % 2 == 0              Optional condition
'''