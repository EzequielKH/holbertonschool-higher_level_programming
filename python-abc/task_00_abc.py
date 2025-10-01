#!/usr/bin/python3
""" """

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, sound):
        self.sound = sound
        def sonar(self):
            print(f"The generic animal says: {animal.sound()}")

class Dog(Animal):
    def __init__(self, sound):
        self.sound = sound
        def sonar2(self):
            print(f"The dog says: {dog.sound()}")

class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound
        def sonar3(self):
            print(f"The cat says: {cat.sound()}")

dog = Dog("Bark")
cat = Cat("Meow")
