__author__ = 'Victoria'

from src.game.Creature import *

#Monsters
class Monster(Creatures, Observable, Observer):
    def __init__(self, name):
        super(Monster, self).__init__()
        self._name = name
        self.ready = None
        self._health = 10
        self._healthMax = 10
        self.attackWeapon = AttackWeapon()
        self.notifyObservers()

    def visit(self, room):
        room.occupy(self)
        room.attack(self)

    def update(self, Observable):
        self.planMove()

