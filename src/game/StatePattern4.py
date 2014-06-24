

class State(object):
    def __init__(self,hero, monster):
        super(State, self).__init__()
        self.hero = hero
        self.monster = monster

    def north(self): pass
    def south(self): pass
    def east(self): pass
    def west(self): pass
    def attack(self): pass
    def run(self): pass
    def rest(self): pass

class RoamState(State):
    def north(self):
        self.currentState = RoamState
        print ("In the roam state north")
    def south(self):
        self.currentState = RoamState
        print ("In the roam state south")
    def east(self):
        self.currentState = RoamState
        print ("In the roam state east")
    def west(self):
        self.currentState = RoamState
        print ("In the roam state west")


class AttackState(State):
    def attack(self):
        self.currentState = AttackState
        print ("Attack state")


class RunState(State):
    def run(self):
        self.currentState = RunState
        print ("Run State")

class RestState(State):
    def rest(self):
        self.currentState = RestState
        print ("I am in the sleeping state")