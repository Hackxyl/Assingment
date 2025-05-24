class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"My name is {self.name}."

class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return f"The {self.species} makes a sound."

class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        return f"The {self.model} is expensive."