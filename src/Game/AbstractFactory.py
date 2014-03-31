__author__ = 'Victoria'

import random

class Inventory:
    """An inventory of weapons and spells"""
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def showInventory(self):
        inventory = self.pet_factory.get_pet()
        print ("This is a lovely", inventory)
        print ("It says", inventory.speak())
        print ("It eats", self.pet_factory.get_food())

# Stuff that our factory makes

class Barbarian:
    def speak(self):
        return "woof"
    def __str__(self):
        return "Dog"

class Dragon:
    def speak(self):
        return "meow"
    def __str__(self):
        return "Cat"

# Factory classes

class DogFactory:
    def get_pet(self):
        return Barbarian()
    def get_food(self):
        return "dog food"

class CatFactory:
    def get_pet(self):
        return Dragon()
    def get_food(self):
        return "cat food"

# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()

# Show pets with various factories
inventory = Inventory()
for i in range(3):
    inventory.pet_factory = get_factory()
    inventory.show_pet()
    print ("=" * 10)