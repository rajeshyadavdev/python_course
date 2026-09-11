""" 
Python functions can return multiple values.

Syntax:
    def function_name():
        return value1,value2
        

1. Multiple values can be returned using commas.
2. Python returns them as a tuple.
3. Returned values can be unpacked into variables.
"""
def min_max(numbers):
    return min(numbers),max(numbers)

min,max = min_max([10,20,30,40])
print(f"Min:{min},Max:{max}")

# Min:10,Max:40