# Concatenation tuple1 + tuple2 Joins tuples
tuple1 = (1,2,3)
tuple2 = (10,20,30)
tuple3 = tuple1 + tuple2
print(tuple3) # (1, 2, 3, 10, 20, 30)


# Repetition tuple1 * 3 Repeats tuple
tuple1 = (1,2,3)
print(tuple1*3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)


# Membership value in tuple1 Checks value exists
tuple1 = (1,2,3)
print(2 in tuple1) # True
print(20 in tuple1) # False


# Length len(tuple1) Counts items
numbers = (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(len(numbers)) # 9

# Slicing tuple1[1:4] Gets part of tuple
numbers = (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(numbers[1:4]) # (2, 3, 1)

