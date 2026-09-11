""" 
A docstring is a string written inside a function to explain what the function does.

"""
# Syntax:
def function_name():
    """Function description."""
    # statement
    
''' 
1. A docstring is written using triple quotes.
2. It is usually written as the first statement inside a function.
3. It explains the purpose of the function.
4. It helps other programmers understand the function.
5. It can be viewed using help() or .__doc__.
'''    
def add_numbers(num1,num2):
    """This function return the sum of two numbers"""
    return num1 + num2

print(add_numbers(10,20))   # 30
print(add_numbers.__doc__)  # This function return the sum of two numbers


# Good Docstring Style
def calculate_area(length,width):
    """ 
    Return the area of rectangle.
    
    length:length of rectangle
    width:width of rectangle
    """
    return length * width

print(calculate_area(8,6))
print(calculate_area.__doc__)

''' 
48

        Return the area of rectangle.
        
        length:length of rectangle
        width:width of rectangle
'''