""" 
Syntax:
  tuple_name[start:end:step]

Explanation
  1. Slicing is used to get a part of a tuple.
  2. The start index is included.
  3. The end index is excluded.
  4. Step controls the gap between selected values.
  5. Slicing returns a new tuple.
  
"""
numbers = (10,20,30,40,50,60,70)
print(numbers[:]) # (10, 20, 30, 40, 50, 60, 70)

print(numbers[1:3]) # (20, 30)

print(numbers[:2])  # (10,  20)

print(numbers[3:])  # (40, 50, 60, 70)

print(numbers[::2]) # (10, 30, 50, 70)

print(numbers[::-1]) # (70, 60, 50, 40, 30, 20, 10)


# Slicing Table
''' 
Code                Meaning                         Result
----                -------                         ------
numbers[1:4]        Index 1 to before 4             (20, 30, 40)

numbers[:3]         Start to before index 3         (10, 20, 30)

numbers[3:]         Index 3 to end                  (40, 50, 60,70)

numbers[::2]        Every second item               (10, 30, 50)

numbers[::-1]       Reverse tuple                   (70,60, 50, 40, 30, 20, 10)

'''


