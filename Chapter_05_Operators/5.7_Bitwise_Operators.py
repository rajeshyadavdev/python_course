""" 
Bitwise operators work on binary numbers.
Binary means numbers written using only:
0 and 1

Computers store numbers internally in binary form.

Example:
Decimal 5 = Binary 101
Decimal 3 = Binary 011
Bitwise operators compare or shift bits


&   => Bitwise AND

`   => `

^   => Bitwise XOR

~   => Bitwise NOT

<<  => Left shift

>>  => Right shif

"""

# Bitwise AND &
# Bitwise AND compares bits.
''' 
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
'''
a = 5
b = 3
print(a & b) # 1

''' 
5 in binary = 1 0 1
3 in binary = 0 1 1

  1   0   1
& 0   1   1
-----------
  0   0   1 => 1 in decimal
  
So: 5 & 3 = 1  
'''

# Bitwise OR |
# Bitwise OR compares bits.
''' 
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
'''

a = 5
b = 3
print(a | b) # 7
''' 
5 in binary = 1 0 1
3 in binary = 0 1 1

  1   0   1
| 0   1   1
-----------
  1   1   1 => 7 in decimal
'''

# Bitwise XOR ^
# Bitwise XOR gives 1 when bits are different.
''' 
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
'''
a = 5
b = 3
print(a ^ b)
''' 
5 in binary = 1 0 1
3 in binary = 0 1 1

  1   0   1
| 0   1   1
-----------
  1   1   0 => 6 in decimal
'''

# Bitwise NOT ~
# Bitwise NOT flips bits. In Python, the result of ~x is:
# ~x = -(x+1)
x = 5
print(~x) # -(5+1) = -6
''' 
Explanation:
~5 = -(5 + 1)
~5 = -6

For beginners, remember:
Bitwise NOT does not simply make 5 into -5.
It gives -(number + 1).
'''

# Left Shift <<
# Left shift moves bits to the left.
# Simple meaning:
# x << n means x multiplied by 2 power n
x = 5
print(x<<1) #10
''' 
Explanation:
5 << 1
5 × 2 = 10

Binary view:
5 in binary = 101
After left shift by 1:
1010
1010 in decimal = 10
'''


# Right Shift >>
# Right shift moves bits to the right.
# Simple meaning:
# x >> n means x divided by 2 power n and gives whole-number result

x = 10
print(x>>1) # 5
''' 
Explanation:
10 >> 1
10 // 2 = 5

Binary view: 10 in binary = 1010
After right shift by 1:
101
101 in decimal = 5
'''




