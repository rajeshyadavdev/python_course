""" 
__enter__ and __exit__ are used to create context managers.Context managers work with
the with statement.

Synatx:

def __enter__(self):
  return self
def __exit__(self, exc_type, exc_value, traceback):
  statement
  
Explanation
1. __enter__ runs at the start of the with block.
2. __exit__ runs when the with block ends.
3. __exit__ runs even if an error occurs inside the with block.
4. __exit__ receives exception details if an error occurs.
5. If __exit__ returns True, the exception is suppressed.
6. If __exit__ returns False or None, the exception continues.  
"""
class SimpleContext:
  def __enter__(self):
    print("Entering")
    return self
  def __exit__(self, exc_type, exc_value, traceback):
    print("Exiting")

with SimpleContext():
  print("Inside with block")


''' 
Entering
Inside with block
Exiting
''' 


