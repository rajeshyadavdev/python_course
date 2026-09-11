""" 
These functions are useful when working with inheritance.

Syntax
  isinstance(object, ClassName)
  issubclass(ChildClass, ParentClass)

1. isinstance() checks whether an object belongs to a class.
2. It also returns True if the object belongs to a child class.
3. issubclass() checks whether one class inherits from another class.
4. Both return True or False
"""
class Animal:
  pass

class Dog(Animal):
  pass

dog = Dog()
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True

