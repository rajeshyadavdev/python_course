""" 
Syntax:
while condition:
    statement

Explanation
1. A while loop runs as long as the condition is True.
2. Before every round, Python checks the condition.
3. If the condition is True, the loop block runs.
4. If the condition becomes False, the loop stops.


FLOW-CHART
---------
Start
    |
    |-->check condition
                |
                |--> True -> execute loop block
                |                       |
                |                       |->check condition again
                |--> False -> loop stop                       
"""
# Example 1: Print numbers from 1 to 5

number = 1
while number <= 5:
    print(number)
    number += 1
''' 
1
2
3
4
5
'''

''' 
for Loop vs while Loop
----------------------
for Loop    
--------
1. Main used to loop over a sequence.
2. Best when number of iterations is known
3. Work with String, range(),and other iterablevalues
4. Stops when Sequence ends                    
5. Risk Usually safer Can create infinite loop


while Loop
----------
1. Main used to repeat while a condition is True.
2. Best when number of iterations is not fixed
3. Work with Conditions
4. Stops when Sequence ends 
5. Stop when Condition becomes False 
6. Risky if condition never becomes False
'''

''' 
When to Use for and while
--------------------------
1. Loop through characters in a string      =>for loop

2. Loop through numbers using range()       =>for loop

3. Repeat until password is correct         =>while loop

4. Repeat while balance is available        =>while loop

5. Repeat fixed number of times             =>for loop

6. Repeat based on condition                =>while loop
'''