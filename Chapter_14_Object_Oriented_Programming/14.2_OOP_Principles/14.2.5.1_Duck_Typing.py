""" 
Duck typing means Python focuses on what an object can do, not its exact type.

Basic Idea
----------
If an object has the needed method, Python can use it.

"""
class Duck:
  def speak(self):
    print("Quack")
    
class Person:
  def speak(self):
    print("Hello") 

def call_speak(obj):
  obj.speak()
  
call_speak(Duck())         
call_speak(Person())   

# Quack
# Hello

''' 
Python does not care whether the object is Duck or Person. It only checks whether speak()
exists.
'''      