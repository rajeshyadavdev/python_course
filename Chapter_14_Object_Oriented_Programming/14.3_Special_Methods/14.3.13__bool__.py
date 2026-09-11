""" 
__bool__ defines truth value behavior of an object.

Synatx:
  def __bool__(self):
    return True_or_False
    
    
Explanation
1. __bool__ is called by bool(obj).
2. It is also used in if obj: conditions.
3. It must return True or False.
4. If __bool__ is not defined, Python may use __len__.
5. If both are missing, most objects are considered True.
    
"""
class Cart:
  def __init__(self, items):
    self.items = items

  def __bool__(self):
    return len(self.items) > 0

cart = Cart(["Book"])
if cart:
  print("Cart has items")

# Cart has items

