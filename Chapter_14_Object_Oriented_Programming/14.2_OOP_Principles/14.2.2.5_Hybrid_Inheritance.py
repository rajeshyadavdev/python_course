""" 
Hybrid inheritance is a combination of two or more types of inheritance.
1. Hybrid inheritance mixes different inheritance types.
2. It can include multiple, multilevel, or hierarchical inheritance together.
3. It is powerful but can become complex.
4. MRO is important in hybrid inheritance.

"""
class Person:
  def show_person(self):
    print("Person")

class Student(Person):
  def show_student(self):
    print("Student")

class Employee(Person):
  def show_employee(self):
    print("Employee")

class TeachingAssistant(Student, Employee):
  def show_task(self):
    print("Teaching Assistant")

task = TeachingAssistant()   

task.show_person()
task.show_student()
task.show_employee()
task.show_task()
''' 
Person
Student
Employee
Teaching Assistant
'''
