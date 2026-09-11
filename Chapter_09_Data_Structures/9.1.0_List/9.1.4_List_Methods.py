""" 


"""
# 1. append() =>Adds one item at the end
items = [1,2,3]
items.append(40)  #Added 40 to items at the end
print(items) #[1, 2, 3, 40]


# 2. extend() =>Adds multiple items 
items = [1,2,3]
items.extend([50, 60])  # Added 50, 60 to items at the end
print(items) # [1, 2, 3, 50, 60]



# 3. insert() =>Adds item at specific index 
items = items = [1,2,3]
items.insert(1, 15) # Added 15 to items at index 1
print(items) # [1, 15, 2, 3]



# 4. remove() Removes first matching value 
items = [1,2,3]
items.remove(2)  # Removes 20
print(items) # [1, 3]
# items.remove(20)  if value 20 is not there in list then we get
# ValueError: list.remove(x): x not in list



# 5. pop() Removes item by index 
items = [1,2,3]
items.pop(1) # Removes item at index 1
print(items) # [1,3]


# 6. clear() Removes all items
items = [1,2,3] 
items.clear() # Empty list
print(items) # []



# 7. index() Returns index of value
items = [1,2,3] 
index = items.index(2) # Gives position/index of given value
print(index) # 1 
# index = items.index(30) if value is not present in list then
# ValueError: 30 is not in list


# 8. count() Counts occurrences 
items = [1,2,3,2,1,2]
count = items.count(2) # Count of 2
print(count) # 3


# 9. sort() Sorts list 
items = [1,2,32,12,34,32,3]
items.sort() # Ascending order
print(items) # [1, 2, 3, 12, 32, 32, 34]


# 10. reverse() Reverses list 
items = [1, 2, 3, 12,]
items.reverse() # Reverse order
print(items) # [12, 3, 2, 1]

# 11. copy() Creates shallow copy 
items = [1,2,3]
new = items.copy()  #New list copy
print(id(items)) # 1981773060352
print(id(new)) # 1981773347456



# Useful Functions with Lists
# 1. len() Counts items 
numbers = [1,2,3,4,5]
length = len(numbers)
print(length) # 5


# 2. sum() Adds numeric items 
numbers = [1,2,3,4,5]
sum_of_number = sum(numbers)
print(sum_of_number) # 15


# 3. min() Smallest value 
numbers = [10,22,30,4,5]
minimum_value = min(numbers)
print(minimum_value) # 4


# 4. max() Largest value 
numbers = [11,32,3,34,25]
maximum_value = max(numbers)
print(maximum_value) # 34


# 5. sorted() Returns sorted copy 
numbers = [12,2,33,4,95]
sorted_list = sorted(numbers)
print(sorted_list) # [2, 4, 12, 33, 95]



