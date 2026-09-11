""" 
Syntax:
for value1,value2 in zip(sequence1,sequence2):
    statement
    
    
Explanation
    1. zip() is used to loop over two or more sequences together.
    2. It takes one item from each sequence at the same time.
    3. The loop stops when the shortest sequence ends.
    
FLOW-CHART
---------
Sequence1:A B C D E
Sequence2:1 2 3 4 5
    |
    zip()
    |
    (A,1)(B,2)(C,3)(D,4)(E,5)
    |
    Loop run pair by pair
    
"""
# Example 1: Zip two strings
letters = "ABCDE"
numbers = "12345"
for letter,number in zip(letters,numbers):
    print(letter,number)


''' 
A 1
B 2
C 3
D 4
E 5
'''


# Example 2: Different length sequences
letters = "ABCDE"
numbers = "123"
for letter,number in zip(letters,numbers):
    print(letter,number)
    
''' 
A 1
B 2
C 3


Explanation:
    1. letters has 5 characters.
    2. numbers has 3 characters.
    3. zip() stops after the shorter sequence ends.
'''    