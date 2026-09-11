""" 
Syntax:
  tuple_name = ([item1, item2], value)

1. A tuple itself is immutable.
2. But if a tuple contains a mutable item like a list, the inner list can be changed.
3. This happens because the tuple is still pointing to the same inner list.

"""

# Example 1
data = ([10, 20], "Python")
data[0][1] = 99
print(data) # ([10, 99], 'Python')

''' 
Explanation Table
-----------------
Part                    Mutable or Immutable?
----                    ---------------------
1.Outer                   tuple Immutable
2.Inner                   list Mutable
3.data[0] = [1, 2]        Not allowed
4.data[0][1] = 99         Allowed

'''

