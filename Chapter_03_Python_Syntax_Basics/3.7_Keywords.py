"""
Keywords
--------
Keywords are reserved words in Python. They already have special meaning, so we cannot
use them as variable names. Some common Python keywords:

Python Keywords: [
  'False', 
  'None', 
  'True', 
  'and', 
  'as', 
  'assert', 
  'async', 
  'await', 
  'break', 
  'class', 
  'continue', 
  'def', 
  'del', 
  'elif', 
  'else', 
  'except', 
  'finally', 
  'for', 
  'from', 
  'global', 
  'if', 
  'import', 
  'in', 
  'is', 
  'lambda', 
  'nonlocal', 
  'not', 
  'or', 
  'pass', 
  'raise', 
  'return', 
  'try', 
  'while', 
  'with', 
  'yield'
  ]
  
  Total Python Keywords: 35
"""
# Python provides a built-in module called keyword.
import keyword
print("Python Keywords:", keyword.kwlist[:])
''' 
Python Keywords: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''


print("Length of Total Python Keywords:", len(keyword.kwlist[:]))
# Length of Total Python Keywords: 35


# This prints the list of Python keywords. To check whether a word is a keyword: 
print(f"Is class is keyword:{keyword.iskeyword("class")}")
# Is class is keyword:True

print(f"Is student is keyword:{keyword.iskeyword("student")}")
# Is student is keyword:False