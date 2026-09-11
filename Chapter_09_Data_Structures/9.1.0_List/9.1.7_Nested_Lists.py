""" 
Syntax:
  list_name = [[item1, item2], [item3, item4]]

Explanation
  1. A nested list means a list inside another list.
  2. It is useful for matrix-like data, rows and columns, or grouped values.
  3. To access nested list values, use multiple indexes.
"""

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matrix[0]) # [1, 2, 3]
print(matrix[1][0]) # 4


# Updating Nested List Value
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix[1][1] = 50
print(matrix) # [[1, 2, 3], [4, 50, 6], [7, 8, 9]]

