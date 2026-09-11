""" 
self refers to the current object.

Syntax
    def method_name(self):
        statement

1. self represents the object that is calling the method.
2. It is used to access object attributes and methods.
3. Python automatically passes the object as self.
4. self is not a keyword, but it is the standard convention.
5. Always use self for instance methods.

"""

class Student:
    def show_name(self):
        print(self.name)
        

student = Student()
student.name = "Rajesh"
student.show_name()   # Rajesh
     