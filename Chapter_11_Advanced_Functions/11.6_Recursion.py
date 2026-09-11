""" 
Recursion means a function calling itself.

Syntax:
    def function_name():
        function_name()


A correct recursive function must have a stopping condition.


1. Recursion is used when a problem can be broken into smaller versions of the same problem.
2. A recursive function calls itself.
3. Every recursion must have a base case.
4. The base case stops the recursion.
5. Without a base case, recursion continues until Python raises RecursionError.


Part                Meaning
====                =======
Base case           Condition that stops recursion
Recursive case      Function calling itself



Function Start
    |
    Check base case
            |
            |--> True --> Stop Recursion
            |
            |--> False --> Call function again
            
"""

# Example 1: Factorial
# Factorial means: 5! = 5 × 4 × 3 × 2 × 1

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

print(factorial(5))  # 120

''' 
factorial(5) = 5 * factorial(4) = 5 * 4 * factorial(3) = 5 * 4 * 3 * factorial(2) = 5 * 4 * 3 * 2 * factorial(1) = 5 * 4 * 3 * 2 * 1 = 120
'''
    
