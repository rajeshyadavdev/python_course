""" 
Indexing means accessing a single character from a string. Every character in a string has a
position number. 
This position number is called an index.

Python indexing starts from 0.
"""

word = "python"

''' 
Index  : 0   1   2   3   4   5
String : p   y   t   h   o   n
'''
print(word[0],end=" ")
print(word[1],end=" ")
print(word[2],end=" ")
print(word[3],end=" ")
print(word[4],end=" ")
print(word[5])

# p y t h o n



# Positive Indexing
# Positive indexing starts from the left side.
''' 
Index  : 0   1   2   3   4   5
String : p   y   t   h   o   n
'''
print(word[0],word[1],word[2],word[3],word[4],word[5])
# p y t h o n


# Negative Indexing
# Negative indexing starts from the right side with -1
''' 
Index  : -6   -5   -4   -3   -2   -1
String :  p    y    t    h    o    n
'''
print(word[-6],word[-5],word[-4],word[-3],word[-2],word[-1])
# p y t h o n

# -1 means last character and -2 means second last character


# Index Error
# If you try to access an index that does not exist, Python gives an error.

print(word[10])
# IndexError: string index out of range

# why ?
# "Python" has indexes from 0 to 5 only. Index 10 does not exist.
