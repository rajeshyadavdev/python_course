""" 
Inheritance vs Composition
==========================
Point           Inheritance                   Composition
-----           -----------                   -----------
Relationship    Is-a                          Has-a
Code style      Child class extends parent    Class contains another object
Example         Dog is an Animal              Car has an Engine
Reuse method    Inherit methods               Use contained object methods
Flexibility     Can become tightly connected  Usually more flexible


Use Inheritance When
=====================
Child really is a type of parent.
Example:Dog is an Animal
Student is a Person


Use Composition When
====================
One object has or uses another object.
Example:
Car has an Engine
Computer has a Processor


Complete Inheritance Types Summary
==================================
Type          Structure               Example
----          ---------               -------
Single        A -> B                  Animal -> Dog

Multilevel    A -> B -> C             Animal -> Dog -> Puppy

Hierarchical  A -> B, A -> C          Animal -> Dog, Animal -> Cat

Multiple      A + B -> C              Father + Mother -> Child

Hybrid        Combination             Person -> Student/Employee -> TeachingAssistant

OOP Principles Summary
======================
Principle             Meaning                             Python Feature
---------             -------                             --------------
Encapsulation         Control access to data              _name, __name, getter/setter,@property

Inheritance           Reuse parent class code             class Child(Parent)

Polymorphism          Same method, different behavior     Overriding, duck typing

Abstraction           Hide implementation details         ABC, @abstractmethod

Composition           Build one object using another      Object inside object


Important OOP Scenario Table
============================
Scenario                                       Use
--------                                       ---
Need to protect data                           Encapsulation

Need to reuse common code                      Inheritance

Need same method with different behavior       Polymorphism

Need to force child class method structure     Abstraction

Need one object inside another                 Composition

Need multiple parent classes                   Multiple inheritance

Need to resolve method search order            MRO

Need parent constructor logic                  super()

Need to check object/class relationship        isinstance(), issubclass()

"""