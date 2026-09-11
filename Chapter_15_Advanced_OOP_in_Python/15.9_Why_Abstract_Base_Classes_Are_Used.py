""" 
Abstract base classes are used when we want to force child classes to implement required
methods.

Every payment class must have pay() method.
UPI payment -> pay()
Card payment -> pay()
Cash payment -> pay()

Benefit                         Explanation
=======                         ============
Common structure                All child classes follow same design
Prevents incomplete classes     Child must implement abstract methods
Improves readability            Required methods are clear
Supports polymorphism           Same method name works across classes

"""