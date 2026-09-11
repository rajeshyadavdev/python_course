""" 
Hierarchical inheritance means multiple child classes inherit from one parent class.

Syntax:
  class Parent:
    pass
  
  class Child1(Parent):
    pass
  
  class Child2(Parent):
    pass
        
"""
class Animal:
  def eat(self):
    print("Eating")

class Dog(Animal):
  def bark(self):
    print("Barking")

class Cat(Animal):
  def meow(self):
    print("Meowing")

dog = Dog()
cat = Cat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()
''' 
Eating
Barking
Eating
Meowing
'''