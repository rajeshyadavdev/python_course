""" 
Syntax:
  list_name[index] = new_value
  
1. Lists are mutable.
2. We can change an existing item using its index.
3. The index must exist in the list.
  
"""

marks = [87,76,80,90]
marks[1] = 99
print(marks) #[87, 99, 80, 90]


# Updating Multiple Values
marks[1:3] = [1,2]

print(marks) #[87, 1, 2,90]