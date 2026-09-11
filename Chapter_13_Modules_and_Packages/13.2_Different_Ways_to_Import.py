""" 
Python provides different import styles.

Import Styles Table
===================
Import Style            Syntax                  Example                     How to Use
------------            ------                  -------                 -   ----------
Normal import           import module           import math                 math.sqrt(25)
Import with alias       import module as alias  import math as m            m.sqrt(25)
Import specific item    from module import item from math import sqrt       sqrt(25)
Import multiple items   from module import a, b from math import sqrt, pow  sqrt(25)
Import all from module  import * from math      import *                    sqrt(25)
"""
from math import sqrt
print(sqrt(36))
# Output: 6.0

# Important Point
# Avoid using from module import * in large programs. It can make code unclear and may cause name conflicts.
