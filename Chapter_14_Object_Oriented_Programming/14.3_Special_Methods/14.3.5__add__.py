""" 
__add__ defines custom behavior for the + operator.


Syntax:
def __add__(self, other):
  return result

1. __add__ is called when obj1 + obj2 is used.
2. It is used for operator overloading.
3. It should return a new result.
4. If the other object type is not supported, return NotImplemented.
5. It should be used only when addition makes logical sense.

"""
class Money:
  def __init__(self, amount):
    self.amount = amount

  def __add__(self, other):
    if not isinstance(other, Money):
      return NotImplemented
    return Money(self.amount + other.amount)

  def __str__(self):
    return f"Amount: {self.amount}"

money1 = Money(100)
money2 = Money(50)
result = money1 + money2
print(result)
# Amount:150
