""" 
Operator overloading means giving custom behavior to operators for user-defined classes.

Explanation
1. Operators like +, -, *, ==, <, and [] can be customized.
2. This is done using special methods.
3. Operator overloading should be logical.
4. Do not overload operators in a confusing way.
5. Operators internally call matching dunder methods.
"""

# Operator Overloading Table
''' 
Operator / Operation                Special Method          Example
====================                ==============          =======
+                                   __add__                 obj1 + obj2
-                                   __sub__                 obj1 - obj2
*                                   __mul__                 obj1 * obj2
/                                   __truediv__             obj1 / obj2
//                                  __floordiv__            obj1 // obj2
%                                   __mod__                 obj1 % obj2
**                                  __pow__                 obj1 ** obj2
==                                  __eq__                  obj1 == obj2
!=                                  __ne__                  obj1 != obj2
<                                   __lt__                  obj1 < obj2
<=                                  __le__                  obj1 <= obj2
>                                   __gt__                  obj1 > obj2
>=                                  __ge__                  obj1 >= obj2
[]                                  __getitem__             obj[index]
()                                  __call__                obj()
len()                               __len__                 len(obj)
str()                               __str__                 str(obj)
repr()                              __repr__                repr(obj)
'''