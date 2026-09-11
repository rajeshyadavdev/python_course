""" 
dir() shows the names available inside a module.

Syntax
  dir(module_name)

Explanation
1. dir() helps us inspect a module.
2. It shows functions, variables, classes, and special names inside the module.
3. It is useful while learning or debugging.
"""
import math
print([m for m in dir(math) if not m.startswith("_")][:10])
# ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb']

# NOTE: dir() does not explain what each name does. For explanation, use help().