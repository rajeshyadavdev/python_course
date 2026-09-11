""" 
Syntax:
  new_list = [expression for item in sequence]

With condition:
new_list = [expression for item in sequence if condition]

1. List comprehension is a short way to create a new list.
2. It is commonly used when each item needs to be processed.
3. It can also filter values using if.
4. It makes code shorter and cleaner.

"""
# Example 1
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
print(squares) # [1, 4, 9, 16, 25]


# Example 2: With Condition
numbers = [1, 2, 3, 4, 5, 6]
even_number = [number for number in numbers if number % 2 == 0]
print(even_number) # [2, 4, 6]


