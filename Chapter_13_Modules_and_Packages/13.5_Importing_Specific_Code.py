""" 
Syntax
  from module_name import function_name

File structure:
===============
project/
│
├── calculator.py
└── main.py

Example 1
==========
calculator.py
-------------
def add(a,b):
  return a+b

def subtract(a,b):
  return a-b
  
main.py
-------
from calculator import add
print(add(10,20))

output:30
    
"""