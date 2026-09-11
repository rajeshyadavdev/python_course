""" 
__contains__ defines behavior for the in operator.

Syntax
  def __contains__(self, item):
    return True_or_False

Explanation
1. __contains__ is called by item in obj.
2. It should return True or False.
3. It is useful for custom container-like classes.

"""

class Team:
  def __init__(self, members):
    self.members = members

  def __contains__(self, member):
    return member in self.members

team = Team(["Aman", "Riya", "Kabir"])
print("Aman" in team) # True
print("Neha" in team) # FAlse


# Important Rules for Special Methods
''' 
Rule                            Explanation
----                            ------------
Return correct type             __str__ and __repr__ must return string
__len__ must return integer     It should return non-negative integer
Use NotImplemented              For unsupported operator types
Avoid confusing behavior        Operators should behave logically
Do not call directly            Use len(obj), not obj.__len__()

Special Methods Summary
=======================
Method        Meaning                     Common Use
======        =======                     ==========
__str__       User-friendly string        print(obj)
__repr__      Developer-friendly string   repr(obj)
__len__       Defines length              len(obj)
__getitem__   Defines indexing            obj[index]
__add__       Defines addition            obj1 + obj2
__sub__       Defines subtraction         obj1 - obj2
__call__      Makes object callable       obj()
__enter__     Starts context manager      with obj:
__exit__      Ends context manager        End of with
__eq__        Equality comparison         obj1 == obj2
__lt__        Less-than comparison        obj1 < obj2
__bool__      Truth value                 if obj:
__iter__      Returns iterator            for item in obj:
__next__      Returns next item           Iterator protocol
__contains__  Membership test             item in obj
'''