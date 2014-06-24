__author__ = 'Victoria'

from src.game.AttackSpell import *

class Room(object):
    def accept(self, visitor):
        visitor.visit(self)
    def occupy(self, occupier):
        print("A room is being visited by", occupier)
    def chest(self, opener):
        print(opener,"has opened the chest.")
    def getItem(self, item):
        print("You have received an %s, from the chest"  % ThunderBolt)
    def north(self, north):
        print(self, "is going north in the room", north)
    def attack(self, occupy):
        print("hero","attacked by", "monster")
    def __str__(self):
        return self.__class__.__name__

class Room1(Room): pass
class Room2(Room): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__

