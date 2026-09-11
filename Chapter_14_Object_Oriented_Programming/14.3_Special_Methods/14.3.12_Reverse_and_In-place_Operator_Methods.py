""" 
Python also supports reverse and in-place operator methods.

Explanation
1. Reverse methods are used when the left object does not support the operation.
2. In-place methods are used for operators like +=, -=, *=.
3. These are advanced but useful to know.

Table
=====
Type                  Example Operator     Method
----                  ----------------     ------
Normal addition       obj + other          __add__
Reverse addition      other + obj          __radd__
In-place addition     obj += other         __iadd__
Normal subtraction    obj - other          __sub__
Reverse subtraction   other - obj          __rsub__
In-place subtraction  obj -= other         __isub__
"""