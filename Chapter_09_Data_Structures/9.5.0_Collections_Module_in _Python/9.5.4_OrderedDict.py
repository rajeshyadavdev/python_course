""" 
OrderedDict is a dictionary that remembers and manages the order of items.

Syntax:
  from collections import OrderedDict
  dictionary_name = OrderedDict()

Explanation
  1. OrderedDict stores key-value pairs in order.
  2. Normal dictionaries also preserve insertion order in modern Python.
  3. OrderedDict is still useful because it has extra order-related methods.
  4. It can move items to the beginning or end.
  5. It can remove items from either side.

"""
from collections import OrderedDict
student = OrderedDict()
student["name"] = "Aman"
student["age"] = 21
student["course"] = "Python"
print(student)
# OrderedDict({'name': 'Aman', 'age': 21, 'course': 'Python'})


# Useful OrderedDict Methods
''' 
Method                     Meaning                   Example
move_to_end(key)           Moves key to the end      data.move_to_end("name")

move_to_end(key,last=False)Moves key to the beginningdata.move_to_end("name",last=False)

popitem()                  Removes last item         data.popitem()

popitem(last=False)        Removes first item        data.popitem(last=False)
'''




''' 
Normal Dictionary vs OrderedDict
================================
Point                         Normal Dictionary          OrderedDict
Preserves insertion order     Yes, in modern Python      Yes
Move key to end               Not directly               Yes
Remove first item easily      Not directly               Yes
Best for                      General dictionary use     Order-sensitive dictionary logic
'''