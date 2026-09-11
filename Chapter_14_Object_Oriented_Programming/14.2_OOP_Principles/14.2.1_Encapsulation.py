""" 
Encapsulation means binding data and methods together inside a class and controlling
how data is accessed or modified.

Basic Idea
==========
Data + Methods = Encapsulation

1. Encapsulation keeps related data and behavior inside one class.
2. It helps protect data from direct unwanted changes.
3. Python does not have strict private variables like Java or C++.
4. Python uses naming conventions to show access level.
5. Encapsulation is commonly handled using:
    1. Public attributes
    2. Protected attributes
    3. Private/name-mangled attributes
    4. Getter and setter methods
    5. @property
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance()) # 1500

# Here, __balance is not directly accessed from outside. It is accessed using methods.



# Public, Protected, and Private Members
''' 
Type                        Syntax   Meaning                            Example
---                         ------   -------                            -------
Public                      name     Can be accessed normally           self.name
Protected                   _name    Meant for internal use             self._salary
Private / Name mangling     __name   Avoid accidental outside access    self.__pin

'''
class Student:
    def __init__(self):
        self.name = "Rajesh"
        self._age = 23
        self.__fees = 2000
        
student = Student()      
print(student.name)  # Rajesh
print(student._age)  # 23

# Direct access to __fees will fail:
# print(student.__fees) 
#AttributeError: 'Student' object has no attribute '__fees'

''' 
Important Point
===============
Double underscore does not make data fully private.
It performs name mangling to avoid accidental access.
Internally, Python changes:
__grade -> _Student__grade
So technically it can still be accessed, but it should not be used directly.
'''
print(student._Student__fees) #2000


''' 
Getter and Setter Methods
=========================
Getter and setter methods are used to read and update private data safely.

Syntax:
    def get_value(self):
        return self.__value
    
    def set_value(self):
        self.__value = value
        
1. Getter method reads private data.
2. Setter method updates private data.
3. Setter can validate data before updating.
4. This protects the object from invalid values.            
'''
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salarys(self):
        return self.__salary
    
    def set_salarys(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")


employee = Employee(8000)
employee.set_salarys(9000)
print(employee.get_salarys()) # 9000





# Encapsulation Using @property
''' 
@property allows a method to behave like an attribute.

Syntax:
    @property
    def attribute_name(self):
        return value
        
1. @property is a clean way to control access to data.
2. It allows validation before changing data.
3. It supports getter and setter behavior.
4. It makes code look simple while still protecting data.
        
'''
class Candidate:
    def __init__(self, marks):
        self.marks = marks
        
    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Marks cannot be negative")
        self._marks = value
        
        
candidate = Candidate(85)
candidate.marks = 95
print(candidate.marks) #95
