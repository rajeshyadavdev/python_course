""" 
deque means double-ended queue.
It allows fast adding and removing from both ends.

Syntax
  from collections import deque
  deque_name = deque(iterable)

1. deque is used when we need fast insert/remove from left and right.
2. It works like a queue and stack.
3. Lists are slower when removing from the beginning.
4. deque is useful for queues, recent history, undo operations, and sliding windows.
"""
# Example 1
from collections import deque
numbers = deque([10, 20, 30])
numbers.append(40)
numbers.appendleft(5)
print(numbers)

# deque([5, 10, 20, 30, 40])

# Common deque Methods
''' 
Method          Meaning                                 Example
append()        Adds item at right end                  d.append(10)
appendleft()    Adds item at left end                   d.appendleft(10)
pop()           Removes item from right end             d.pop()
popleft()       Removes item from left end              d.popleft()
extend()        Adds multiple items at right            d.extend([1, 2])
extendleft()    Adds multiple items at left             d.extendleft([1, 2])
rotate(n)       Rotates items                           d.rotate(1)
clear()         Removes all items                       d.clear()

'''

# List vs deque
''' 
Point                       List                      deque
Add at end                  Fast                      Fast
Remove from end             Fast                      Fast
Add at beginning            Slower                    Fast
Remove from beginning       Slower                    Fast
Best for                    General storage           Queue operations
'''