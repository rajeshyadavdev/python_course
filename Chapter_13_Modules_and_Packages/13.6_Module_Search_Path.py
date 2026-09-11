""" 
When we import a module, Python searches for it in specific locations.

Explanation
===========
Python searches in this general order:
1. Current working directory.
2. Paths listed in PYTHONPATH, if set.
3. Standard library directories.
4. Installed third-party package directories.
"""
import sys
print(sys.path)
# PS C:\Users\Admin\Desktop\oneweek\python\Complete_Python> 

