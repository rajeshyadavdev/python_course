""" 
Special methods are predefined methods in Python with double underscores before and
after their names.
They are also called:
    ● Special methods
    ● Magic methods
    ● Dunder methods
    
dunder means double underscore.

Synatx 
    def __method_name__():
        statement
       
       
Explanation
    1. Special methods allow objects to work with Python’s built-in operations.
    2. They are called automatically by Python.
    3. They usually start and end with double underscores.
    4. We normally do not call them directly.
    5. Instead, we use operators or built-in functions.

Example Idea
    print(obj) -> calls obj.__str__()
    
    len(obj) -> calls obj.__len__()
    
    obj[0] -> calls obj.__getitem__(0)
    
    obj1 + obj2 -> calls obj1.__add__(obj2)
        
"""

# Common Special Methods Table
''' 
Special Method              Triggered By            Purpose
==============              ============            ========

__init__        ClassName()                 Initializes object
__str__         str(obj), print(obj)        User-friendly string
__repr__        repr(obj)                   Developer-friendly string
__len__         len(obj)                    Returns length
__getitem__     obj[index]                  Indexing/slicing
__add__         obj1 + obj2                 Addition
__sub__         obj1 - obj2                 Subtraction
__call__        obj()                       Makes object callable
__enter__       with obj:                   Starts context manager
__exit__        End of with block           Exits context manager

'''