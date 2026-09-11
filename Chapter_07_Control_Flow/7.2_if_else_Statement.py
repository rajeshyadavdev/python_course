""" 
Syntax:

if condition:
    when_statement_True
else:
    when_statement_False
    
 
Explanation
The if-else statement is used when we want to run one block if the condition is True and
another block if the condition is False.
Only one block runs.
If the condition is True, the if block runs.
If the condition is False, the else block runs. 

FLOW_CHART
----------
Start
|
|---True---> execute_if_block
|
|---False---> execute_else_block
|
Rest of program
       
"""

age = 20
if age>=18:
    print("You are eligible to vote..")
else:
    print("You are not eligible to vote")
    
print("Rest of program")        

# You are eligible to vote..
# Rest of program
