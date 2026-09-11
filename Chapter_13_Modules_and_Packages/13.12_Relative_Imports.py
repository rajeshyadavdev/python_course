""" 
A relative imports code based on the current module’s location inside a package.

Syntax
from .module import name
from ..package import module

Explanation
1. Relative imports use dots.
2. One dot . means current package.
3. Two dots .. means parent package.
4. Relative imports are used inside packages.
5. They are not meant for simple standalone scripts.




Syntax      Meaning
======      =======
.           Current package
..          Parent package
...         Grandparent package

Example Structure
-----------------
project/
│
└── app/
├── __init__.py
├── calculator.py
└── reports.py

Inside reports.py:
from .calculator import add

This means: Import add from calculator.py in the same package

NOTE:Important Point
====================
Relative imports work properly when the module is part of a package. They may fail if the file
is run directly as a script.

Better way to run a package module:
-----------------------------------
python -m app.reports

"""