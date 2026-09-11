""" 
The if statement is used when we want to run some code only when a condition is True.
If the condition is True, Python executes the indented block.
If the condition is False, Python skips the indented block.

syntax:
if condition:
    statement


FLOW-CHART
----------
Start
  |
Check Condition
|        |
|        |--True-->Execute if block
|        |
|        |--False-->Skip if block
|
Continue rest of code.            
"""

# Example-1
age = 20
if age>=18:
    print("You are eligible to vote..")
print("Rest of program.")    

# You are eligible to vote..
# Rest of program.



# Example-2
marks = 50
is_student = True

if marks>=40 and is_student:
    print("Your are students and Passed..")
print("Rest of program")    

# Your are students and Passed..
# Rest of program

