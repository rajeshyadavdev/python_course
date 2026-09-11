""" 
__getitem__ defines indexing and slicing behavior.


Syntax:
def __getitem__(self, index):
  return value

1. __getitem__ is called when we use obj[index].
2. It allows custom objects to support indexing.
3. It can also support slicing. It is useful for custom sequence-like classes.
4. If implemented carefully, it can also help an object work in loops.

"""
class Team:
  def __init__(self, members):
    self.members = members

  def __getitem__(self, index):
    return self.members[index]

team = Team(["RCB", "MI", "DC","CSK","KKR"])
print(team[0])   # RCB
print(team[1])   # MI
print(team[0:2]) # ['RCB','MI']

print(team[::-1]) # ['KKR', 'CSK', 'DC', 'MI', 'RCB']
