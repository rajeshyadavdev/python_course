""" 
A Python file can be used as a module.

File Structure
==============
project/
│
├── calculator.py
└── main.py

calculator.py
-------------
def add(a, b):
  return a + b
  
main.py
-------
import calculator

result = calculator.add(10, 20)
print(result)

# Output: 30

Explanation
1. calculator.py is a module.
2. main.py imports the calculator module.
3. The function add() is accessed using calculator.add().
4. Both files should be in the same folder for this simple import to work.

"""