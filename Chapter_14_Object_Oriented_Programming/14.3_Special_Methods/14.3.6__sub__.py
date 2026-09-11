""" 
__sub__ defines custom behavior for the - operator.

Syntax
  def __sub__(self, other):
    return result

1. __sub__ is called when obj1 - obj2 is used.
2. It is also part of operator overloading.
3. It should return a meaningful result.
4. Return NotImplemented if the other type is unsupported.

"""
class Money:
  def __init__(self, amount):
    self.amount = amount

  def __sub__(self, other):
    if not isinstance(other, Money):
      return NotImplemented
    return Money(self.amount - other.amount)

  def __str__(self):
    return f"Amount: {self.amount}"

money1 = Money(100)
money2 = Money(40)
result = money1 - money2
print(result)
# Amount: 60

