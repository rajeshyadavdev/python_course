""" 
Multilevel inheritance means a class inherits from a child class, forming a chain.

Syntax:

class A:
  pass

class B(A):
  pass

class C(B):
  pass    
"""
class Animal:
  def eat(self):
    print("Eating")

class Dog(Animal):
  def bark(self):
    print("Barking")
    
class Puppy(Dog):
  def weep(self):
    print("Weeping")
puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.weep()
# Eating
# Barking
# Weeping

