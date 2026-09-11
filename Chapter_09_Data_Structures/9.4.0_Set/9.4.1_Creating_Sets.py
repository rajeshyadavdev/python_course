""" 
Syntax:
  set_name = {item1, item2, item3}

1. Sets can store numbers, strings, Booleans, and tuples.
2. Sets cannot store mutable values like lists or dictionaries.
3. Empty set must be created using set(). {} creates an empty dictionary, not an empty set.

"""

numbers = {1,2,3,4,5}
names = {"Rakesh","Ramesh","Rajesh"}
mixed = {"Rajesh",12,123.23,True}
empty_set = set()

print(numbers)   # {1, 2, 3, 4, 5}
print(names)     # {'Ramesh', 'Rakesh', 'Rajesh'}
print(mixed)     # {True, 123.23, 12, 'Rajesh'}
print(empty_set) # set()

# Order may differ in output.


''' 
Different Ways to Create Sets
=============================
Type                    Example
----                    ------
Empty set               items = set()
Number set              marks = {80, 90, 75}
String set              names = {"Aman", "Riya"}
Mixed set               data = {"Aman", 20, True}
From list               items = set([10, 20, 10])
From string             letters = set("ABC")
From tuple              items = set((10, 20, 30))
''' 

# Empty Set Important Point
a = {}
b = set()
print(type(a)) # <class 'dict'>
print(type(b)) # <class 'set'>

