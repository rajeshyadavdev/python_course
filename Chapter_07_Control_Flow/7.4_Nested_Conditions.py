""" 
Syntax:
with if only
------------
if condition1:
    if condition2:
        statement
        

with if-else
------------        
if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3        


Nested condition means writing one condition inside another condition. The inner condition is
checked only when the outer condition is True. This is useful when one decision depends on
another decision.

FLOW-CHART
----------
Start
|
|-->check outer condition1
|       |
|       |--->False--> execute outer block and skips inner condition
|       |   
|       |--->True
                |--->check inner condition2
                                    |
                                    |--> execute inner if block
                                    |
                                    |--> execute inner else block

"""

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("Id required")    
else:
    print("Entry not Allowed")        
    
    
# Entry Allowed
 