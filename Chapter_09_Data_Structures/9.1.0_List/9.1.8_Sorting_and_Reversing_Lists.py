""" 
Sorting means arranging values in order. Reversing means changing the order from last to
first.
"""
# Sorting and Reversing Table
# 1. Sort ascending numbers.sort()
# Changes Original List? Yes.
# Result => Small to large
numbers = [2,4,6,3,5,7,1]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5, 6, 7]


# 2. Sort descending numbers.sort(reverse=True) 
# Changes Original List? Yes 
# Result => Large to small
numbers = [2,4,6,3,5,7,1]
numbers.sort(reverse=True)
print(numbers) # [7, 6, 5, 4, 3, 2, 1]


# 3. Sorted copy sorted(numbers) 
# Changes Original List? No 
# Result => Returns new sorted list
numbers = [2,4,6,3,5,7,1]
sorted_number = sorted(numbers)
print("Original numbers:",numbers) # Original numbers: [2, 4, 6, 3, 5, 7, 1]
print("Sorted numbers:",sorted_number) # Sorted numbers: [1, 2, 3, 4, 5, 6, 7]



# 4. Reverse original numbers.reverse() 
# Changes Original List? Yes 
# Result => Reverses same list
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers) # [5, 4, 3, 2, 1]


# 5  Reverse copy numbers[::-1] 
# Changes Original List? No 
# Result => Returns reversed copy
numbers = [1,2,3,4,5]
reverse_numbers = numbers[::-1]
print("Original numbers:",numbers) # Original numbers: [1, 2, 3, 4, 5]
print("reversed numbers:",reverse_numbers) # reversed numbers: [5, 4, 3, 2, 1]



# sort() vs sorted()
''' 
Point               sort()                      sorted()
------              ------                      --------
1. Type                List method                 Built-in function

2. Original list       Changes original list       Does not change original list

3. Return value        Returns None                Returns new sorted list

4. Usage               numbers.sort()              sorted(numbers)
'''
