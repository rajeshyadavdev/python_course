""" 
Comparison operators are used to compare two values. The result of a comparison is
always a Boolean value:
● True
● False

1)==    => Equal to     => 10 == 10

2)!=    =>Not equal to  =>  10 != 5

3)>     =>Greater than  =>  10 > 5

4)<     =>Less than     =>  5 < 10

5)>=    =>Greater than or equal to  =>  10 >= 10

6)<=    =>Less than or equal to   =>5 <= 10

"""
# Equal To ()==)
# The == operator checks whether two val
print(10 == 10) # True
print(10 == 5)  # False


# Not Equal To !=
# The != operator checks whether two values are not equal.
print(10 != 5) # True
print(10 != 10) # False

''' 
Explanation:
10 != 5 True because 10 is not equal to 5
10 != 10 False because 10 is equal to 10
'''



# Greater Than (>)
# The > operator checks whether the left value is greater
print(10 > 5) # True
print(5 > 10) # False

# Less Than (<)
# The < operator checks whether the left value is less than the right value
print(10 < 5) # False
print(5 < 10) # True



# Greater Than or Equal To >=
# The >= operator checks whether the left value is greater than or equal to the right value.
print(10 >= 5) # True
print(10 >= 10) # True
print(5 >= 10) # False


# Explanation:
# 10 >= 5 True because 10 is greater than 5
# 10 >= 10 True because 10 is equal to 10
# 5 >= 10 False



# Less Than or Equal To <=
# The <= operator checks whether the left value is less than or equal to the right value.
print(5 <= 10) # True
print(10 <= 10) # True
print(10 <= 5) # False


# Explanation:
# 5 <= 10 True because 5 is less than 10
# 10 <= 10 True because 10 is equal to 10
# 20 <= 10 False



# Comparison with Variables
a = 15
b = 20
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True



