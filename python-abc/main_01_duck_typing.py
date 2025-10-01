#!/usr/bin/python3
""" """



from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, sound):
        self.sound = sound
        def sonar(self):

    pass
class Dog(animal):
    def __init__(self, sound):
        self.sound = sound
        def sonar2(self):
    pass

class Cat(animal):
    def __init__(self, sound):
        self.sound = sound
        def sonar3(self):

dog = Dog()
cat = Cat()
animal = Animal()
print(f"The dog says: {dog.sound()}")
print(f"The cat says: {cat.sound()}")
print(f"The generic animal says: {animal.sound()}")
    pass