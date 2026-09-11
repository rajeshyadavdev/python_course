""" 
__init__.py is a special file used in Python packages.

Explanation
1. __init__.py is placed inside a package folder.
2. It tells Python that the folder is a regular package.
3. It can be empty.
4. It can also contain package-level initialization code.
5. It can control what is exposed when importing from the package.

mypackage/
├── __init__.py
├── calculator.py
└── messages.py

Example 1
mypackage/__init__.py
---------------------
from .calculator import add

main.py
-------
from mypackage import add
print(add(10, 20))


Output: 30
"""
