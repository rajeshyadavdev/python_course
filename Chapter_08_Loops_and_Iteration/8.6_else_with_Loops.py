
"""

Syntax:

for variable in sequence:
    statement
else:
    statement_after_loop 
    

Syntax:

while condition:
    statement
else:
    statement_after_loop    
      
      
Explanation
    1. A loop can have an else block. The else block runs when the loop finishes normally.
    2. If the loop stops because of break, the else block does not run      
    
     
"""

# Example 1: Loop finishes normally
for number in range(1,4):
    print(number)
else:
    print("loop finished")    
    
''' 
1
2
3

loop finished
'''
    
# Example 2: Loop stops with break
for number in range(1, 5):
    if number == 3:
        break
    print(number)
else:
    print("Loop finished")
    
''' 
1
2

Here else block will not execute
'''    