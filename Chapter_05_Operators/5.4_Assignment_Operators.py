""" 
Assignment operators are used to assign values to variables.
The most basic assignment operator is: =


=     => x = 10     => x = 10

+=    => x += 5     => x = x + 5

-=    => x -= 5     => x = x - 5

*=    => x *= 5     =>  x = x * 5

/=    => x /= 5     => x = x / 5

//=   => x //= 5    => x = x // 5

%=    => x %= 5     => x = x % 5

**=   => x **= 5    => x = x ** 5
"""

# Basic Assignment =
x = 10
print(x)  # 10


# Add and Assign +=
x = 10
x += 5
print(x) # 15

''' 
Explanation:
x += 5
Same as:
x = x + 5
'''

# Subtract and Assign -=
x = 10
x -= 5
print(x) # 5

''' 
Explanation: 
x -= 3
Same as: 
x = x - 3
'''


# Multiply and Assign *=
x =  10
x *= 2
print(x) # 20

''' 
Explanation: 
x *= 2
Same as: 
x = x * 2
'''


# Divide and Assign /=
x = 10
x /= 2
print(x) # 5.0
''' 
Important: /= gives float result because / gives float result.

'''


# Floor Divide and Assign //=
x = 10
x //= 3
print(x) # 3
''' 
Explanation:
x //= 3
Same as:
x = x // 3
'''

# Modulus and Assign %=
x = 10
x %= 3
print(x)  # 1
''' 
Explanation: 
x %= 3
Same as: 
x = x % 3

'''


# Power and Assign **=
x = 2
x **= 3
print(x) # 8

''' 
Explanation: 
x **= 3
Same as: 
x = x ** 3
'''