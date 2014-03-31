__author__ = 'Victoria'

# Demonstration of "visitor" pattern.
from __future__ import generators
import random

# The Room hierarchy cannot be changed:
class Room(object):
    def accept(self, visitor):
        visitor.visit(self)
    def occupy(self, occupier):
        print(self, "room visited by", occupier)
    def open(self, opener):
        print(self, "chest opened by", opener)
    def attack(self, attacker):
        print(self, "you were attacked by", attacker)
    def __str__(self):
        return self.__class__.__name__

class Room1(Room): pass
class Room2(Room): pass
class Room3(Room): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class Creature(Visitor): pass
class Hero(Creature): pass
class Monster(Creature): pass

class Barbarian(Hero):
    def visit(self, room):
        room.occupy(self)
        room.open(self)

class Dragon(Monster):
    def visit(self, room):
        room.occupy(self)
        room.attack(self)

def CastleRoomGen(n):
    castleRooms = Room.__subclasses__()
    for i in range(n):
        yield random.choice(castleRooms)()


bar = Barbarian()
drag = Dragon()
for room in CastleRoomGen(10):
    room.accept(bar)
    room.accept(drag)
