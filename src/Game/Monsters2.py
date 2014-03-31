__author__ = 'Victoria'
#from src.game.Creature import *
from src.common.Observable import *
from src.game.Room2 import *
from src.game.StatePattern4 import *
from random import *

class Monster(Observable, Observer, Room):
    def __init__(self, name):
        super(Monster, self).__init__()
        self._name = name
        self.ready = None
        self._health = 1
        self._healthMax = 10
        self.roamState = RoamState(self,name)
        self.attackState = AttackState(self, name)
        self.runState = RunState(self,name)
        self.restState = RestState(self,name)
        self.currentState = None
        self.setRoam()

    def accept(self, visitor):
        visitor.visit(self)
    def visit(self, room):
        room.monster(self)
        room.occupy(self)

    def roam(self):
        self.ready = True
        print ("%s am a monster roaming" % self._name)
        self.notifyObservers()
        #self.doDamage()

    def doDamage(self):
        self.damage = min(
            max(randint(0, 2) - randint(0, 2), 0),
            self._health)
        self._health -= self.damage
        if self.damage == 0:
            print ("monster avoids heros's attack.")
        else:
            print ("hero injures monster!")
            self._health -= 1
            if self._health <= 0:
                print ("Monster died!")


    def act(self):
        if self.ready:
            self.roam()
            self.ready = False

    def update(self, Observable):
        self.roam()
    def display(self):
        print ("%s am a monster about to attack you!" % self._name)


    def northB(self):
        self.ready = True
        self.currentState.north()
    def south(self):
        self.ready = True
        self.currentState.south()
    def east(self):
        self.ready = True
        self.currentState.east()
    def west(self):
        self.ready = True
        self.currentState.west()

    def setRoam(self):
        self.currentState = self.roamState
    def setAttack(self):
        self.currentState = self.attackState
    def northward(self):
        self.currentState.north()
    def west(self):
        self.currentState.west()
    def east(self):
        self.currentState.east()
    def south(self):
        self.currentState.south()
    def attacking(self):
        self.currentState.attack()
