"""
Python File Structure
---------------------92
Python programs are usually saved with the .py extension.
Example: hello.py

Inside hello.py:
print("This is my first python file")

A Python file can be very simple. It may contain only one line of code. But in larger programs, we usually follow a clean structure.

"""
# Basic file structure:

# 1. Comments or program Description

# 2. Imports
import math

# 3. Variable
radius = 5

# 4. Constants Variable
PI = math.pi

# 5. Logic
area = PI*radius*radius

# 6. Output
print(f"Area of circle: {area}")

# Area of circle: 78.53981633974483

'''
Program File
|
|-Comments
|
|-Imports
|
|-Variables
|
|-Logic or Processing
|
|-Output

Important point:
---------------
Python does not force a fixed file structure for small programs. But writing code in a clean
order makes it easier to read and maintain.
'''
