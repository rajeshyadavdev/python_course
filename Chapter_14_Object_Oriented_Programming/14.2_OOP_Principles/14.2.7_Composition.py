""" 
Composition means one class contains an object of another class.

Basic Idea
==========
NOTE:Inheritance = is-a relationship

NOTE:Composition = has-a relationship

1. Composition is used when one object is made of another object.
2. It represents a has-a relationship.
3. It is often preferred over inheritance when there is no true is-a relationship.

"""
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()

car = Car()
car.start() # Engine started

''' 
Explanation:
    Car has an Engine.
    So this is composition.
'''

# Association, Aggregation, & Composition
''' 
Relationship   Meaning                                                  Example
============   =======                                                  =======
Association    One class uses another class                             Teacher teaches Student
Aggregation    One class has another, but both can exist independently  Department has Teachers
Composition    One class owns another strongly                          House has Rooms

'''

# Important Difference
''' 
Point                           Aggregation                 Composition
=====                           ===========                 ===========
Relationship                    Weak has-a                  Strong has-a
Child object can exist alone?   Yes                         Usually no
Example                         Team has Players            Car has Engine
'''