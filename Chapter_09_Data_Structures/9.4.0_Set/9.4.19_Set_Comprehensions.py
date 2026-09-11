""" 

Syntax
  new_set = {expression for item in sequence}

With condition:
  new_set = {expression for item in sequence if condition}

1. Set comprehension is a short way to create a set.
2. It is similar to list comprehension.
3. It automatically keeps only unique values.
4. It can include conditions

"""      

numbers = [1, 2, 2, 3, 4, 4]
square = {number*number for number in numbers}
print(square)
# Output: {16, 1, 4, 9} :Duplicate input values do not create duplicate set values.

numbers = [1, 2, 3, 4, 5, 6]
even_number = {number for number in numbers if number % 2 == 0}
print(even_number) # {2, 4, 6}

''' 
List Comprehension vs Set Comprehension
=======================================
Point               List Comprehension       Set Comprehension
-----               ------------------       -----------------
Brackets            []                       {}
Allows duplicates   Yes                      No
Ordered             Yes                      No fixed order
Result type         List                     Set
Example             [x for x in data]        {x for x in data}
'''