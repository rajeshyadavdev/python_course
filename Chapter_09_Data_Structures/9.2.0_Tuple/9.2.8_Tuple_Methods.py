# count() Counts how many times a value appears 
items = (1,2,1,4,1) 
print(items.count(1)) # 3

print(items.count(10)) # 0  as 10 is not present so we get 0


# index() Returns index of first matching value
items = (10,20,30,40) 
print(items.index(20)) # 1

# print(items.index(90))  # ValueError: tuple.index(x): x not in tuple



# Useful Functions with Tuples
numbers = (100,20,3,4,50,6)
# len() Counts items len(numbers)
print(len(numbers)) # 6

# sum() Adds numeric items sum(numbers)
print(sum(numbers)) # 183

# min() Smallest value min(numbers)
print(min(numbers)) # 3

# max() Largest value max(numbers)
print(max(numbers)) # 100

# sorted() Returns sorted list sorted(numbers)
print(sorted(numbers)) # [3, 4, 6, 20, 50, 100]


