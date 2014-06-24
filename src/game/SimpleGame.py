__author__ = 'Victoria'
from src.common.Observable import *
from src.game.AttackSpell import *
from random import *

class HeroState(object):
    def __init__(self, name):
        self._name = name
        super(HeroState, self).__init__()
    def north(self): pass
    def south(self): pass
    def attack(self): pass

class RoamState(HeroState):

    def north(self):
        self.currentState = RoamState
        print ("In the roam state going north")
    def south(self):
        self.currentState = RoamState
        print ("In the roam state going south")

class AttackState(HeroState):
    def attack(self):
        self.currentState = AttackState
        print ("Attack state")

class Hero(Observable,Observer, AttackSpell):
    def __init__(self, name):
        super(Hero, self).__init__()
        self._name = name
        self.ready = None
        self._health = 10
        self._healthMax = 10
        self.roamState = RoamState(self)
        self.attackState = AttackState(self)
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
                self.monster.attack()
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
                        monst.doDamage()
                        if monst._health >= 0:
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
        print(Hero,"attacked by", Monster)
    def __str__(self):
        return self.__class__.__name__

class Room1(Room):pass
class Room2(Room): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class Monster(Observable, Observer):
    def __init__(self, name):
        super(Monster, self).__init__()
        self._name = name
        self.ready = None
        self._health = 1
        self._healthMax = 10
        self.roamState = RoamState(self)
        self.attackState = AttackState(self)
        self.currentState = None
        self.setRoam()
    def accept(self, visitor):
        visitor.visit(self)
    def visit(self, room):
        room.monster(self)
        room.occupy(self)
    def roam(self):
        self.ready = True
       # self.currentState.north()
        print ("%s am a monster roaming" % self._name)
        self.notifyObservers()
    def attack(self):
        self.ready = True
        self.currentState.attack()
        print ("%s am a monster attacking youuu!" % self._name)
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
    def healthStatus(self):
        print ("%s's health: %d/%d" % (self._name, self._health, self._healthMax))

    def update(self, Observable):
        self.roam()
    def setRoam(self):
        self.currentState = self.roamState
    def northward(self):
        self.currentState.north()
    def setAttack(self):
        self.currentState = self.attackState
    def attacking(self):
        self.currentState.attack()
    def display(self):
        print ("%s am a monster about to attack you!" % self._name)


if __name__ == '__main__':
    hero = Hero('hero')
    room = Room1()
    monst = Monster('monster')
#    state = hero.roamState.attack()
   # state = hero.attackState.attack()
  #  state = hero.roamState.north()
    hero.addObserver(monst)
    monst.addObserver(hero)
  #  hero.south()
    hero.roam()
   # hero.attacked()
  #  hero.attack()
  #  monst.roam()
 #   room.accept(hero)
 #   monst.attack()
  #  monst.doDamage()
   # hero.healthStatus()
  #  monst.healthStatus()
  #  room.attack(monst)
