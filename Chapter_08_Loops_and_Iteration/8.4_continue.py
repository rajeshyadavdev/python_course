""" 
Syntax:
    continue

Explanation
    1. continue skips the current round of the loop.
    2. It does not stop the full loop.
    3. After continue, Python moves to the next round.
    
FLOW-CHART
----------
start loop
    |
    condition inside loop
    |
    |-->continue found-->skip current round and continue with next round
    |
    |-->no continue-->execute remaining code    
"""
# Example 1: Skip number 3
for number in range(1,6):
    if number == 3:
        continue
    print(number)
    
''' 
1
2
4
5


Explanation:
    1. When number is 3, continue runs.
    2. print(number) is skipped for 3.
    3. The loop continues with 4 and 5.
'''    