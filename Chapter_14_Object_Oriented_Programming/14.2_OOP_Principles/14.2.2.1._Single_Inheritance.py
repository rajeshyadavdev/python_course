''' 
Single inheritance means one child class inherits from one parent class.

Synatx:

class Parent:
    pass

class Child(Parent):
    pass  
      
'''
class Animal:
  def eat(self):
    print("Eating")

class Dog(Animal):
  def bark(self):
    print("Barking")

dog = Dog()
dog.eat()
dog.bark()

# Eating
# Barking

