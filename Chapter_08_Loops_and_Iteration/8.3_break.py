""" 
Syntax:
    break
    
Explanation
1. break is used to stop a loop immediately.
2. When Python sees break, it exits the loop.
3. Code after the loop continues no

FLOW-CHART
----------
loop start
    |
condition inside loop
    |
    |--> break found-->exit loop
    |
    |-->no break-->continue loop
     
"""
# Example 1: Stop loop when number is 4
for number in range(1,8):
    if number==4:
        break
    print(number)
''' 
1
2
3


Explanation:
    1. The loop starts from 1.
    2. When number becomes 4, break runs.
    3. The loop stops before printing 4.
'''    