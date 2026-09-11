""" 
Inheritance allows one class to reuse the properties and methods of another class.

Synatx:
    class ChildClass(ParentClass):
        statement

Explanation
1. Inheritance supports code reuse.
2. The parent class is also called base class or superclass.
3. The child class is also called derived class or subclass.
4. The child class can use parent class attributes and methods.
5. The child class can also define its own attributes and methods.
6. The child class can override parent methods.
7. Inheritance represents an is-a relationship.
        
"""

class Animal:
    def eat(self):
        print("eating")
        
class Dog(Animal):
    
    def bark(self):
        print("barking")
        

dog = Dog()
dog.eat()   # eating
dog.bark()  # barking


# Why Inheritance is Used
''' 
Use                     Meaning
===                     =======
Code reuse              Child class reuses parent code
Extensibility           Child class can add new features
Maintainability         Common logic stays in parent class
Polymorphism            Same method can behave differently
Real-world modeling     Represents is-a relationship.




Example:
Dog is an Animal
Car is a Vehicle
Student is a Person
'''   
                

# Types of Inheritance in Python
''' 
Python supports these major types of inheritance:

Type                        Meaning
====                        ========
Single inheritance          One child inherits from one parent
Multilevel inheritance      Child inherits from parent, and another child inherits from that child
Hierarchical inheritance    Multiple child classes inherit from one parent
Multiple inheritance        One child inherits from multiple parents
Hybrid inheritance          Combination of two or more inherit
''' 

