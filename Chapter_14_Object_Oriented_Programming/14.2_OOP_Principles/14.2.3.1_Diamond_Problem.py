""" 
The diamond problem happens when a child class inherits from two classes that both inherit
from the same parent.

1. Class B and class C both inherit from A.
2. Class D inherits from both B and C.
3. If the same method exists in multiple classes, Python uses MRO to decide.
4. Python handles this safely using MRO.
5. super() also follows MRO.

"""
class A:
  def show(self):
    print("A")

class B(A):
  def show(self):
    print("B")

class C(A):
  def show(self):
    print("C")

class D(B,C):
  pass

d = D()
d.show() #B
# Because the MRO is:
# D -> B -> C -> A -> object

