""" 
Syntax:

if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    default else block
    

Explanation
-----------
elif means else if.
It is used when we need to check multiple conditions. Python checks conditions from top
to bottom. The first condition that becomes True gets executed. After that, Python skips the
remaining conditions.
The else block runs only when all previous conditions are False.    

FLOW_CHART
----------
Start
|
|--->check condition1
|           |
|           |-->True--> execute block1   
|           |
|           |-->False
|                  |
|                  |-->check condition2
|                               |
|                               |-->True--> execute block2
|                               |
|                               |-->False
                                       |
                                       |--> execute else block          
"""

marks = 89
if marks >100:
    print("Invalide Mark")
elif marks >= 90:
    print("Grade-A++")
elif marks >= 80:
    print("Grade-A")
elif marks >= 70:
    print("Grade-B++")
elif marks >= 60:
    print("Grade-B")
elif marks >= 50:
    print("Grade-C++")
elif marks >= 40:
    print("Grade-C")
else:
    print("Failed")
    
    
    
    
    
