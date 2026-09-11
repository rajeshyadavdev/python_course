""" 
Polymorphism means the same method or operation behaves differently for different objects.

Explanation
1. Polymorphism means “many forms”.
2. The same method name can work differently in different classes.
3. Python supports polymorphism through:
    1. Method overriding
    2. Duck typing
    3. Operator overloading

"""

class Dog:
  def sound(self):
    print("Bark")

class Cat:
  def sound(self):
    print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
  animal.sound()
  
''' 
Bark
Meow
'''  

# Polymorphism Types in Python
''' 
Type                  Meaning                                         Example
====                  =======                                         =======
Method overriding     Child changes parent method                     Dog.sound()
Duck typing           Object is accepted if it has required method    animal.sound()
Operator overloading  Operator works differently by class             obj1 + obj2
'''
