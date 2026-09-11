""" 
__len__ defines the behavior of len(obj).


Synatx:
  def __len__(self):
    return integer

Explanation
1. __len__ is called by len(obj).
2. It must return a non-negative integer.
3. It is useful for custom container-like classes.
4. If __bool__ is not defined, Python may use __len__ to decide truthiness.
5. If __len__ returns 0, the object is considered False in Boolean context.
    
"""
class Team:
  def __init__(self, members):
    self.members = members
  
  def __len__(self):
    return len(self.members)
  
teams = Team(["CSK","RCB","MI"])  
  
print(len(teams))  # 3

''' 
if we comment __len__ function we get errors as
TypeError: object of type 'Team' has no len()
'''