
from src.common.Observable import*
from src.game.AttackSpell import *
from src.game.AttackWeapon import *
from src.game.Attributes import *
from src.game.visit import *
from src.game.Heroes import *
#from src.game.AttackInventory import*
from random import*

class Creatures(Observable, GameAttributes, Visitor):
    def __init__(self):
        super(Creatures, self).__init__()
        self._attackSpell = AttackSpell()
        self._attackWeapon = AttackWeapon()
        self._name = ''
        self.gameAttributes = GameAttributes()
        self.health = 1
        self.healthMax = 1

    def doDamage(self, monster):
        self.damage = min(
            max(randint(0, 2) - randint(0, monster.health), 0),
            monster.health)
        monster.health -= self.damage
        if self.damage == 0:
            print ("%s avoids heros's attack." % monster)
        else:
            print ("hero injures %s!" % monster)
        return monster.health <= 0


    def setAttStr(self, strength, con, dex, intt):
        self.Strength = strength
        self.Constitution = con
        self.Dexterity = dex
        self.Intelligence = intt

    def setAttackSpell(self, attackSpell):
        self.attackSpell = attackSpell

    def setAttackWeapon(self, attackWeapon):
        self.attackWeapon = attackWeapon

    def AttackSpell(self):
        self.attackSpell()

    def AttackWeapon(self):
        self.attackWeapon.attackWeapon()

    def planMove(self):
        self.ready = True

    def roam(self):
        print ("%s is roaming around the castle" % self._name)
        self.notifyObservers()

    def act(self):
        if self.ready:
            self.roam()
            self.ready = False

    def north(self):
        print ("%s is moving in the direction north" % self._name)
        self.roam()
        self.notifyObservers()

    def south(self):
        print ("%s is moving in the direction south" % self._name)
        self.roam()

    def east(self):
        print ("%s is moving in the direction east" % self._name)
        self.roam()

    def west(self):
        print ("%s is moving in the direction west" % self._name)
        self.roam()

    def Display(self):
        pass