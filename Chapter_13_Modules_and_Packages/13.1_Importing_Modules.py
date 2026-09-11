""" 
A module is a Python file containing reusable code.
A package is a folder that contains multiple modules.

Module -> single .py file

Package -> folder containing modules

Example:
math.py -> module
my_package/ -> package

Why Modules and Packages Are Used
=================================
1. To organize large programs.
2. To reuse code.
3. To avoid writing the same logic again.
4. To separate code into meaningful files.
5. To use built-in Python features from the standard library.



Importing means using code from another module.

Synatx:
  import module_name

1. import loads a module.
2. After importing, we can use functions, classes, and variables from that module.
3. We access module members using dot . notation.
4. Import statements are usually written at the top of the file.

"""
import  math
print(math.sqrt(25))
# Output: 5.0 => Here, math is a module and sqrt() is a function inside it.