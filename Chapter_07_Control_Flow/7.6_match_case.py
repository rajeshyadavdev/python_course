""" 
Syntax:
match value:
    case pattern1:
        statement1
    case pattern2:
        statement2
    case _:
        statement_default_case        



Explanation
match-case is used to compare one value with multiple possible cases. It is similar to
checking many fixed options.
The _ case works like a default case. It runs when no other case matches. match-case was
introduced in Python 3.10


FLOW-CHART
----------
Start
|
Take value
    |
    |-->match with case1
                |
                |--> match--> execute case1
                |
                |--> not match
                        |
                        |--> match with case2
                                    |
                                    |--> match --> execute case2
                                    |
                                    |--> not match
                                            |
                                            |
                                            execute default case
                        
"""

day = 6
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")   
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")  
    case 5:
        print("Friday") 
    case 6:
        print("Saturday")  
    case 7:
        print("Sunday")  
    case _:
        print("Unknown command")    
                                  