"""
Operator precedence means the order in which Python solves operators.
"""
result = 10 + 5 * 2
print(result) # 20
''' 
A beginner may think:
10 + 5 = 15
15 * 2 = 30

But Python does multiplication first.

Correct solving:
10 + 5 * 2
10 + 10
20

So the result is 20.
'''

''' 
Priority        Operators         Meaning
------------------------------------------
1                 ()              Parentheses

2                 **              Power

3             +x, -x, ~x          Unary plus, unary minus, bitwise NOT

4             *, /, //, %         Multiplication, division, floor division, modulus

5                 +, -            Addition, subtraction

6               <<, >>            Bitwise shifts

7                 &               Bitwise AND

8                 ^               Bitwise XOR

9                 ` `

10          ==, !=, >, <, >=, <=  Comparisons

11               not              Logical NOT

12               and              Logical AND

13                or              Logical OR
'''