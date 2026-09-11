""" 
Loops are used when we want to run the same code multiple times.

Q: Print numbers from 1 to 5
Without a loop, we write many print() statements. With loop, we write the logic once and
Python repeats it

Syntax:

for variable in sequence:
    statemnt
    
    
Explanation
1. A for loop is used to repeat code over a sequence.
2. A sequence can be a string, range, list, tuple, etc.
3. In each round, Python takes one value from the sequence.
4. The loop stops automatically when all values are finished.


FLOW-CHART
----------
Start
|
|
Take next item from sequence
|
|
Is item available in sequence?
    |
    |-->Yes--> execute next item
    |                   |
    |                   |-->Go to next item
    |-->No-->stop loop    
"""
# Example 1: Loop through a string
word = "python"
for letter in word:
    print(letter)
    
''' 
p
y
t
h
o
n
'''    
 
# Example 2: Loop with range()
for num in range(0,6):
    print(num) 

''' 
0
1
2
3
4
5
'''
    
    