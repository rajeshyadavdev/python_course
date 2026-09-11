""" 
Syntax:
for index, value in enumerate(sequence):
    statement
    
Explanation
    1. enumerate() gives both index and value while looping.
    2. It is useful when we need the position of each item.
    3. The index starts from 0 by default.
    
    
FLOW-CHART
----------
sequence
    |
    enumerate()
    |
    Gives index + value
    |
    loop block executed
            
"""
# Example 1: Enumerate a string
word = "python"
for index,value in enumerate(word):
    print(index,value)

''' 
0 p
1 y
2 t
3 h
4 o
5 n
'''


# Example 2: Start index from 1
for index,value in enumerate(word,start=1):
    print(index,value)
    
''' 
1 p
2 y
3 t
4 h
5 o
6 n
'''   


# enumerate() vs Normal Loop
'''
Normal Loop                             enumerate()
-----------                             ------------
1. Gives only value                     Gives index and value

2. Good when index is notneeded         Good when index is needed

3. Simple for direct looping            Better for position-based output
'''
 