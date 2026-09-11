""" 
Method overriding means a child class defines a method with the same name as a parent
class method.

Syntax:
    class Parent:
        def method():
            statement
    
    class Child(Parent):
        def method():
            new_statement
                    

Explanation
1. The method name is the same in parent and child.
2. The child class provides its own version.
3. When called on child object, child method runs.
4. This supports polymorphism.
5. Parent method can still be called using super().

"""
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
        
dog = Dog()
dog.sound() # Bark
