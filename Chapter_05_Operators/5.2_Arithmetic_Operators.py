""" 
Arithmetic operators are used to perform mathematical operations.
1. Addition(+)
2. Subtraction(-)
3. Multiplication(*)
4. Division(/)
5. Power(**)
6. Remainder(%)

Arithmetic operators work mostly with numbers.
"""

# Addition (+)
# The + operator adds two numbers.

a = 12
b = 10
result = a + b
print(result) #22


# Subtraction (-)
# The - operator subtracts one number from another.
a = 22
b = 11
result = a - b
print(result) #11



# Multiplication (*)
# The * operator multiplies two numbers.
a = 2
b = 3
result = a * b
print(result) # 6



# Division (/)
# The / operator divides one number by another. Division using / always gives a float result.

a = 10
b = 2
result = a / b
print(result) #2.0
print(type(result)) #<class 'float'>

# Even though 10 / 5 is mathematically 2, Python gives 2.0.
# That means the result is a float.


# Floor Division (//)
# The // operator divides and gives the whole-number part.

a = 10
b = 5
result1 = a / b
print(result1) # 2.0
print(type(result1)) #<class 'float'>

result2 = a // b
print(result2) # 2
print(type(result2)) #<class 'int'>




# Modulus (%)
# The % operator gives the remainder after division.
a = 10
b = 3
result = a % b
print(result)  # 1
print(type(result)) # <class 'int'>

# 10 divided by 3 => 3 goes into 10 three times: 3 × 3 = 9 Remainder: 10 - 9 = 1



# Exponent / Power (**)
# The ** operator is used to calculate power.

result  = 2 ** 3
print(result) # 8

# Explanation: 2 ** 3 means 2 raised to the power 3



