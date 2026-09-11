""" 
Point                 List            Tuple             Set
-----                 ----            -----             ---
Brackets              []              ()                {}
Ordered               Yes             Yes               No fixed order
Mutable               Yes             No                Yes
Allows duplicates     Yes             Yes               No
Indexing              Yes             Yes               No
Slicing               Yes             Yes               No
Best for              Changeable      Fixed             Unique 
Example               [10, 20]        (10, 20)          {10,20}
"""

''' 
Important Set Operations Table
==============================
Operation           Code                      Meaning
---------           ----                      -------
Create set          items = {10, 20, 30}      Creates set
Empty set           items = set()             Creates empty set
Add one item        items.add(40)             Adds one value
Add multiple items  items.update([40, 50])    Adds many values
Remove safely       items.discard(20)         Removes without error
Remove with error   items.remove(20)          Error if missing
Random remove       items.pop()               Removes random item
Empty set           items.clear()             Removes all items
Check value         10 in items               Membership check
Union               a|b
Intersection        a & b                     Common values
Difference          a - b                     Values in a, not in b
Symmetric difference a ^ b                    Non-common values
Subset              a <= b                    Checks subset
Superset            a >= b                    Checks superset
Copy set            items.copy()              Creates shallow copy
Frozen set          frozenset(items)          Immutable set
'''