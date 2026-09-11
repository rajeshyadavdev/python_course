""" 
When an iterator has no more values, Python raises StopIteration.

"""
# Example 1: Iterator ends
word = "AB"
iterator = iter(word)
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration errors



# Infinite Loop
''' 
An infinite loop is a loop that never stops. 
This usually happens when the condition in a while loop never becomes False.
'''
# Example 1: Infinite loop
number = 1
while number <=5:
    print(number)

''' 
number starts as 1 => condition is number <= 5 => number is never increased=> condition
always stays True . loop never stops

'''   

# correct way
number = 1
while number <=5:
    print(number)
    number +=1 
    
''' 
1
2
3
4
5
'''
    