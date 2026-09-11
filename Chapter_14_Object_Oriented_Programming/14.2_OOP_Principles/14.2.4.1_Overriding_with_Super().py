class Animal:
  def sound(self):
    print("Animal sound")

class Dog(Animal):
  def sound(self):
    super().sound()
    print("Bark")

dog = Dog()
dog.sound()
''' 
Animal sound
Bark
'''
