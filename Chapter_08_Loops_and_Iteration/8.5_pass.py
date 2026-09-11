""" 
Syntax:
    pass
pass means “do nothing”. 
It is used when Python needs a statement, but we do not want to write logic yet. 
It does not stop or skip the loop like break or continue.


FLOW-CHART
----------
start loop
    |
    pass found
            |
            do nothings
                |
                continue with normal execution
"""
# Example 1: Empty loop block
for number in range(1,6):
    pass

# Output: No output appears because pass does nothing.


# Example 2: Placeholder inside condition
for number in range(1,6):
    if number == 2:
        pass
    print(number)
''' 
1
2
3
4
5

'''    

# Loop Control Statements Comparison
''' 
Statement |  Meaning       |         Effect on Loop        |      Common Use
--------------------------------------------------------------------------
break       Stop the loop          Exits the loop completely    Stop when required value is found
continue    Skip current round     Moves to next iteration      Skip unwanted values
pass        Do nothing             No effect on loop            Temporary placeholder
'''

