__author__ = 'Victoria'

from src.common.Observable import *
from src.game.AttackSpell import *
from src.game.Room2 import *
from src.game.StatePattern4 import *
from src.game.Monsters2 import *
from random import *

class Hero(Observable,Observer, AttackSpell):
    def __init__(self, name):
        super(Hero, self).__init__()
        self._name = name
        self.ready = None
        self._health = 10
        self._healthMax = 10
        self.roamState = RoamState(self,name)
        self.attackState = AttackState(self, name)
        self.currentState = None
        self.setRoam()
        self.notifyObservers()

    def __str__(self):
        return self.__class__.__name__

    def northB(self):
        self.ready = True
        self.currentState.north()

    def south(self):
        self.ready = True
        self.currentState.south()

    def roam(self):
        self.ready = True
        if self.currentState:
            d = input( "What direction would you like to go in north or south? \n")
            if d == "north":
                self.currentState.north()
            if d == 'south':
                self.currentState.south()
            if randint(0,1):
                print ("%s comes across a monster!" % self._name)
                self.monster = Monster(self)
                self.monster.display()
                self.monster.attack(self)
                self.attacked()

    def attacked(self):
        self.ready = True
        self.currentState.attack()

        while self.currentState is not self.roamState:
        #  while self.currentState != self.roamState:
            print ("%s is being silly, there is nothing to attack!" % self._name)
            pass
        else:
            self.ready = True
            if self.currentState:
                print ("How would you like to attack the %s?" % Monster)
                text = input("spell or weapon? \n")
                if text == 'spell':
                    useSpell = input("Would you like to use fireball, thunderbolt, or shield \n")
                    if useSpell == 'fireball':
                        print ("%s attacked the monster with a %s" % (self._name, FireBall()))
                        self.monster.doDamage()
                        if self.monster._health >= 0:
                            self.attacked()

    def setRoam(self):
        self.currentState = self.roamState
    def setAttack(self):
        self.currentState = self.attackState
    def northward(self):
        self.currentState.north()
    def south(self):
        self.currentState.south()
    def attacking(self):
        self.currentState.attack()

    def act(self):
        if self.ready:
            self.ready = False
            self.northward()
        if self.ready:
            self.attacking()
            self.ready = False

    def accept(self, visitor):
        visitor.visit(self)
    def visit(self, room):
        room.occupy(self)
        print ("Would you like to open the chest?")
        text = input("yes or no \n")
        if text == 'yes':
            room.chest(self)
        if text == 'no':
            pass
        room.attack(self)
        room.chest(self)
        room.getItem(self)

    def healthStatus(self):
        print ("%s's health: %d/%d" % (self._name, self._health, self._healthMax))

    def update(self, Observable):
        self.northward()
        self.south()
        self.attacking()