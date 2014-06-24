__author__ = 'Victoria'

from src.game.Creature import *
from src.game.Monsters import *
from src.game.Attributes import *
from src.game.StatePattern3 import *
from random import*

class Hero(Creatures, Observable, Observer, GameAttributes, HeroState):
    attackState = None
    roamState = None
    runState = None
    restState = None

    def __init__(self, name):
        super(Hero, self).__init__()
        self._name = name
        self.ready = None
        self.monster = None
        self.attackSpell = AttackSpell()
        self.attackWeapon = AttackWeapon()
        self._state = " "
        self._health = 10
        self._healthMax = 10
        self.roamState = RoamState(self)
        self.runState = RunState(self)
        self.attackState = AttackState(self)
        self.restState = RestState(self)
        self.currentState = self._state
        self.notifyObservers()

    def update(self, Observable):
        self.planMove()

    def getAttributes(self, attributes):
        self.Strength = attributes
        self.Constitution = attributes
        self.Dexterity = attributes
        self.Intelligence = attributes

    def setRoamState(self):
        self.currentState = self.roamState
    def setRunState(self):
        self.currentState = self.runState
    def setAttackState(self):
        self.currentState = self.attackState
    def setRestState(self):
        self.currentState = self.restState

    def attack(self):
        self.currentState = AttackState
        if self._state != '':
            print ("%s is being silly, there is nothing to attack!" % self._name)
        else:
            if self.currentState:
                self.changeState()
                if self._state == 'attack':
                    print ("How would you like to attack the monster? ")
                    text = input("spell or weapon? \n")
                    if text == 'spell':
                        useSpell = input("Would you like to use fireball, thunderbolt, or shield \n")
                        if useSpell == 'fireball':
                            print ("%s attacked the monster with a %s" % (self._name,FireBall()))
                        if useSpell == 'thunderbolt':
                            print ("%s attacked the monster with a %s" % (self._name,ThunderBolt()))
                        if useSpell == 'shield':
                            print ("%s attacked the monster with a %s" % (self._name,SpiritShield()))
                    if text == 'weapon':
                        useWeapon = input("Would you like to use an ax, bow, or sword? \n")
                        if useWeapon == 'ax':
                            print ("%s attacked the monster with a %s" % (self._name,Ax()))
                        if useWeapon == 'bow':
                            print ("%s attacked the monster with a %s" % (self._name,BowArrow()))
                        if useWeapon == 'sword':
                            print ("%s attacked the monster with a %s" % (self._name,Sword()))

                if self.doDamage(self.monster):
                    print ("%s killed the monster" % self._name)
                    print ("%s gains experience" % self._name)
                    self.Experience += 1
                    if self.Experience > 5:
                        self.IncreaseLevel()
                        self._state = 'roam'


    def roam(self):
        self._state = 'roam'
        self.currentState = RoamState
        if self.currentState:
            self.changeState()
            print ("%s is roaming around!" % self._name)
            self.notifyObservers()
            if randint(0, 1):
                self.monster = Monster(self)
                print ("%s comes across a monster!" % self._name)
                self._state = 'attack'

    def run(self):
        self._state = 'running'
        self.currentState = RunState
        if self.currentState:
            self.changeState()
            print ("%s is running around.. as a consequence health is decreasing " % self._name)
            self._health = max(1, self._health - 1)
            if randint(0, 1):
                self.monster = Monster(self)
                print ("%s comes across a monster!" % self._name)
                self._state = 'attack'
                if self._health <=1:
                    self.quit()

    def rest(self):
        if self._state != 'roam':
            print ("A monster is attacking you can not rest!")
            self._state = 'attack'
            if randint(0, 1):
                self.monster = Monster(self)
                print ("%s is being attacked by a monster!" % self._name)
                self.state = 'attack'
        else:
            self._state = 'rest'
            self.currentState = RestState
            if self.currentState:
                self.changeState()
                print ("%s is sleeping." % self._name)
                self._health = max(1, self._health + 1)


    def accept(self, visitor):
        visitor.visit(self)

    def visit(self, room):
        room.occupy(self)
        print ("Would you like to open the chest?")
        room.chest(self)

    def castleRoom(self):
        print ("%s is now in a castle room " % self._name)
        self.notifyObservers()

    def healthStatus(self):
        print ("%s's health: %d/%d" % (self._name, self._health, self._healthMax))

    def levelStatus(self):
        print ("%s's level: %s" % (self._name, self.Level))

    def experStatus(self):
        print ("%s's experience: %s" % (self._name, self.Experience))

    def quit(self):
        print ("%s does not survive and dies." % self._name)
        self._health = 0

    def Display(self):
        print ("You are a Hero!")

