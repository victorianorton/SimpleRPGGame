__author__ = 'Victoria'

from src.game.AttackSpell import *
from src.game.AttackWeapon import *

class HeroState(object):
    def __init__(self):
        super(HeroState, self).__init__()
        self._state = ' '
    def changeState(self):
        print ("changing  state to %s" % self._state)

class AttackState(HeroState):
    def __init__(self, attack):
        super(AttackState, self).__init__()
        self._state = 'attack'
        self._name = 'attack'

    def changingState(self):
        print ("changing state %s" % self._name)
        self.changeState()

class RoamState(HeroState):
    def __init__(self):
        super(RoamState, self).__init__()
        self._state = 'roam'

    def changeState(self):
        print ('changing state %s')

class RunState(HeroState):
    def __init__(self, run):
        super(RunState, self).__init__()
        self._state = 'running'
        self._name = 'running'

    def changingState(self):
        print ("changing state %s" % self._name)
        self.changeState()

class RestState(HeroState):
    def __init__(self, rest):
        super(RestState, self).__init__()
        self._state = 'rest'
        self._name = 'sleeping'

    def changeState(self):
        print ("changing state %s" % self._name)

