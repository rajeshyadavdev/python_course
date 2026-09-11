""" 
Syntax:
range(start)
range(start,stop)
range(start,stop,step)


Explanation
  1. range() creates a sequence of numbers.
  2. It is commonly used with for loops.
  3. The stop value is excluded.
  4. step controls the gap between numbers.
  
  
FLOW-CHART
----------
range() create number
  |
  for loop take one number
  |
  loop block is executed
  |
  Next number is taken
  
"""
# Example 1: range(stop)
for number in range(5):
  print(number)

''' 
0
1
2
3
4

Explanation:
1. range(5) starts from 0.
2. It stops before 5 means 5 is excluded.
'''


# Example 2: range(start, stop)
for number in range(1,5):
  print(number)

''' 
1
2
3
4
'''


# Example 3: range(start, stop, step)
for number in range(2,10,2):
  print(number)
  
''' 
2
4
6
8
'''  


#Negative Step in range()
for number in range(5,1,-1):
  print(number)

''' 
5
4
3
2
'''

# More
for number in range(10,0,-2):
  print(number)
  
''' 
10
8
6
4
2
'''  