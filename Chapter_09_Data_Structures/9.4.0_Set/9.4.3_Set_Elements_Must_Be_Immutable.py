""" 
Syntax
set_name = {immutable_value1, immutable_value2}

Explanation
    1. Set elements must be hashable.
    2. Immutable values like numbers, strings, and tuples can be stored in a set.
    3. Mutable values like lists, dictionaries, and sets cannot be stored in a set.
    4. This is because sets internally need stable values to check uniqueness.
"""
valid_set = {10, "Python", (1, 2)}
print(valid_set) # {10, (1, 2), 'Python'}


# Invalid example:
invalid_set = {[1, 2], [3, 4]}
print(invalid_set) # TypeError: unhashable type: 'list'



# Allowed vs Not Allowed Table
''' 
Value Type        Allowed in Set?                           Example
----------        --------------                            -------
Integer           Yes                                       {10, 20}
Float             Yes                                       {10.5, 20.5}
String            Yes                                       {"A", "B"}
Boolean           Yes                                       {True, False}
Tuple             Yes, if tuple contains immutable items    {(1, 2)}
List              No                                        {[1, 2]}
Dictionary        No                                        {{"a": 1}}
Set               No                                        {{1, 2}}
'''