""" 
defaultdict is a dictionary that gives a default value when a key does not exist.

Syntax
from collections import defaultdict
dictionary_name = defaultdict(default_type)

Explanation
  1. Normal dictionaries give KeyError if a key does not exist.
  2. defaultdict avoids this problem.
  3. It automatically creates a default value for missing keys.
  4. Common default types are int, list, and set.


Flow Chart
Access dictionary key
  |
  key exist?
      |
      |-->Yes--->Return value
      |-->No---->Create default value
      
"""

# Example 1: Using int
from collections import defaultdict
marks = defaultdict(int)
marks["math"] += 10
marks["science"] += 20
print(marks)
# defaultdict(<class 'int'>, {'math': 10, 'science': 20})
# Here, missing keys start with default value 0.



# Common Default Types
''' 
Default           Type Default Value            Common Use
-------           ------------------            ----------
int               0                             Counting
list              []                            Grouping values
set               set()                         Grouping unique values
str               ""                            Empty text
'''

# Example 2: Using list
students = defaultdict(list)
students["Python"].append("Aman")
students["Python"].append("Riya")
students["Java"].append("Kabir")
print(students) 
# defaultdict(<class 'list'>, {'Python': ['Aman', 'Riya'], 'Java': ['Kabir']})
# Normal Dictionary vs defaultdict

''' 
Point                     Normal Dictionary                     defaultdict
-----                     ----------------                      -----------
Missing key               Gives KeyError                        Creates default value
Best for                  Simple key-value data                 Grouping/counting
Needs manual checking     Yes                                   No
'''
