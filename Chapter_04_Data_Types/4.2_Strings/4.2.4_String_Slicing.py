""" 
Slicing means taking a part of a string.

Syntax: string[start:end:step]

start index is included. end index is excluded

start => default 0
end => defult last index
step => default 1

"""
word = "PYTHON"

''' 
string : P  Y  T  H  O  N 
index  : 0  1  2  3  4  5
'''

# start with index 0, end with last index(5) and step with 1
print(word[::]) # PYTHON


# start with index 0, end with last index(4) and step with 1
print(word[0:4]) # PYTH

# start with index 1, end with last index(4) and step with 1
print(word[1:4]) # YTH

# start with index 2, end with last index(6) and step with 1
print(word[2:6]) # THON



# Leaving Start Empty
# If start is empty, Python starts from the beginning index = 0

# start with index 0, end with last index(4) and step with 1
print(word[:4]) # PYTH


# Leaving End Empty
# If end is empty, Python goes till the end index.

# start with index 2, end with last index and step with 1
print(word[2:]) # THON



# Full Slice
# start with index 0, end with last index and step with 1
print(word[:]) # PYTHON

# Slicing with Negative Index
''' 
string :  P   Y   T   H   O   N
index  : -6  -5  -4  -3  -2  -1      
'''
# start with index -3, end with last index and step with 1
print(word[-3:]) # HON



# Slicing with Step
# string[start:end:step]
number = "123456789"
# start with index 1, end with last index and step with 2
print(number[1::2]) # 2468

print(number[::-1]) #987654321
# Explanation: [::-1] means read the string from right to left

