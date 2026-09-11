""" 
Abstraction means hiding internal implementation and showing only essential features.
Explanation
1. Abstraction focuses on what an object does.
2. It hides how the object does it internally.
3. Python supports abstraction using abstract base classes.
4. Abstract base classes are created using the abc module.
5. A class with abstract methods cannot be instantiated directly.
6. Child classes must implement abstract methods.

"""
from abc import ABC, abstractmethod

class Payment(ABC):
  @abstractmethod
  def pay(self,amount):
    pass
  
class UpiPayment(Payment):
  def pay(self, amount):
    print("Paid", amount, "using UPI")

payment = UpiPayment()

payment.pay(2000)
# Paid 2000 using UPI

''' 
Important Point
===============
Payment cannot be used directly because it has an abstract method.
This gives an error:
payment = Payment()
Output:
TypeError: Can't instantiate abstract class Payment with abstract method pay
'''

# Encapsulation vs Abstraction

''' 
Point        Encapsulation                            Abstraction
=====        =============                            ===========
Meaning      Protecting and controlling data          Hiding implementation details
Focus        Data access                              Essential behavior
Achieved by  Private variables, methods, @property    Abstract classes, interfaces
Example      Hide __balance                           Define pay() without showing payment logic
'''

# Encapsulation = How data is protected
# Abstraction = How unnecessary details are hidden

