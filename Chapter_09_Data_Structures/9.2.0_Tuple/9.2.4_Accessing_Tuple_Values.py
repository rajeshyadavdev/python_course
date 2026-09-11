""" 
Syntax
  tuple_name[index]

1. Tuple values are accessed using index numbers.
2. Python indexing starts from 0.
3. Positive indexing starts from the left.
4. Negative indexing starts from the right.

Index Diagram
-------------
tuple_name: ("Rajesh","Rakesh","Ramesh")
+ve_index :     0         1       2
-ve_index :    -3        -2      -1
"""

# Example 1
students = ("Aman", "Riya", "Kabir", "Neha")
print(students[1])   # Riya
print(students[2])   # Kabir
print(students[-1])  # Neha


