""" 
An absolute import uses the full path from the project/package root.

Synatx:
from package.module import name

Explanation
1. Absolute imports are clear and easy to understand.
2. They show the full location of the imported module.
3. They are generally preferred in larger projects.
4. They reduce confusion compared to complex relative imports.

Example 1
Inside main.py:
--------------
from app.calculator import add

This means:
----------
From package app, inside module calculator, import add
"""