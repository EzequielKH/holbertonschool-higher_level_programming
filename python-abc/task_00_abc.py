#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, sound):
        self.sound_value = sound

    def sound(self):
        return self.sound_value


class Dog(Animal):

    def __init__(self, sound="Bark"):
        super().__init__(sound)


class Cat(Animal):

    def __init__(self, sound="Meow"):
        super().__init__(sound)
