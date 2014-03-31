# Demonstration of "visitor" pattern.
import random

class Room(object):
    def accept(self, visitor):
        visitor.visit(self)

    def occupy(self, occupier):
        print(self, "room is being visited by", occupier)

    def chest(self, opener):
        print("chest has been opened by", opener)

    def attack(self, attacker):
        print("attacked by", attacker)

    def __str__(self):
        return self.__class__.__name__

class Outside(object):
    def accept(self, visitor):
        visitor.visit(self)

    def occupy(self, occupier):
        print(self, "you are outside", occupier)

    def pickUp(self, item):
        print(self, "you have retrived an item", item)

    def __str__(self):
        return self.__class__.__name__


class Dungeon(object):
    def accept(self, visitor):
        visitor.visit(self)

    def occupy(self, occupier):
        print(self, "you are in the dungeon", occupier)

    def attack(self, attacker):
        print(self, 'you are being attacked by the dragon!', attacker)

    def __str__(self):
        return self.__class__.__name__

class Room1(Room): pass
class Room2(Room): pass
class Room3(Room): pass
class Outside1(Outside): pass
class Dungeon1(Dungeon): pass


class Visitor:
    def __str__(self):
        return self.__class__.__name__

def CastleRoomGen(n):
    castleRooms = Room.__subclasses__()

    for c in range(n):
        yield random.choice(castleRooms)()

def Outdoors():
    outside = Outside.__subclasses__()
    return outside

def Dungeon():
    dungeon= Dungeon.__subclasses__()
    return dungeon


