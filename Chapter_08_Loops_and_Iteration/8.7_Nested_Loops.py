""" 

Syntax:
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        statement
        

Explanation
    1. Nested loop means one loop inside another loop.
    2. The outer loop runs first.
    3. For every one round of the outer loop, the inner loop runs completely.
    4. Nested loops are useful for patterns, tables, rows and column.
    
"""
# Example 1: Row and column output

for row in range(1,3):
    for column in range(1,3):
        print(row,column)
        
''' 
1   1
1   2
2   1
2   2
'''        
# Example 2: Simple pattern
for row in range(1,5):
    print("*"*row)
    
''' 
*
**
***
****
'''   

 