""" 
*args is used when we do not know how many positional arguments will be passed.

Synatx:
    def function_name(*args):
        statement
        

1. *args collects extra positional arguments.
2. The collected values are stored as a tuple.
3. The name args is a convention; the * is important.
4. Use *args when the number of arguments is flexible.


FLOW_CHART
==========
Function call has many positional arguments
|
v
*args collects them
|
v
Values are stored as a tuple
"""
def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total +=number
    return total


print(add_numbers(1,2,3,4))  # 10
print(add_numbers(10,20,30,40))  # 100

# Here, numbers behaves like a tuple.
