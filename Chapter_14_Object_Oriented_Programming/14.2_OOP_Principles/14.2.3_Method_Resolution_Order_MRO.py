""" 
MRO is the order Python follows while searching for methods in inheritance.

Syntax:
  ClassName.mro()
  or
  ClassName.__mro__

1. MRO decides which method is called first.
2. It is important in multiple inheritance.
3. Python uses the C3 linearization algorithm for MRO.
4. The search starts from the child class.
5. Then Python checks parent classes according to MRO.
6. Finally, it checks the base object class.

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
  # def show(self):
  #   print("D") 
  pass
             
    

object = D()

object.show()    # B
print(D.mro())

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# MRO Flow
# D -> B -> C -> A -> object

# Since B comes before C, B.show() runs.


