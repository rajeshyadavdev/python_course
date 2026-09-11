""" 
A package is a folder containing Python modules.

Basic Package Structure
=======================
project/
│
├── main.py
│
└── mypackage/
├── __init__.py
├── calculator.py
└── messages.py

Explanation
-----------
1. mypackage is a package.
2. calculator.py and messages.py are modules inside the package.
3. __init__.py marks the folder as a regular Python package.
4. main.py can import modules from the package.


Example 1
mypackage/calculator.py
----------------------
def add(a, b):
  return a+b
  
main.py
-------
from mypackage.calculator import add

print(add(10, 20))


Output: 30  
"""