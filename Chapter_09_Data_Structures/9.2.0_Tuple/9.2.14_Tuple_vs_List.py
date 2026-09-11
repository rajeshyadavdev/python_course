
""" 
Point                       List                  Tuple
-----                       ----                  -----
Brackets                    Uses []               Uses ()
Mutability                  Mutable               Immutable
Can update items            Yes                   No
Can add/remove items        Yes                   No
Speed Slightly slower       Slightly              faster
Best for                    Data that may change  Data that should not change

"""
''' 
Important Tuple Operations Table
--------------------------------
Operation                   Code                      Meaning
---------                   ----                      -------
Create tuple                items = (10, 20, 30)      Creates tuple

Single-item                 tuple item = (10,)        Creates tuple with one item

Access item                 items[0]                  Gets first item

Slice tuple                 items[1:3]                Gets part of tuple

Count item                  items.count(10)           Counts value

Find index                  items.index(20)           Finds position

Pack tuple                  data = "Aman", 21         Packs values

Unpack tuple                name, age = data          Extracts values

Concatenate                 a + b                     Joins tuples

Repeat                      a * 2                     Repeats tuple

Check membership            10 in items               Returns True or False

Convert list to tuple       tuple(my_list)            Creates tuple

Convert tuple to list       list(my_tuple)            Creates list
'''