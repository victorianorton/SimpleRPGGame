__author__ = 'Victoria'

class Attributes(object):
    def attributes(self):
        pass

class Strength(Attributes):
    def attributes(self):
        print ("I have strength")

class Constistution(Attributes):
    def attributes(self):
        print ("I have constitution ")

class Dexteritiy(Attributes):
    def attributes(self):
        print ("I have dexteritiy ")

class Intelligence(Attributes):
    def attributes(self):
        print ("I have intelligence ")


class GameAttributes(object):
    def __init__(self):
        super(GameAttributes,self).__init__()
        self.Strength = [10]
        self.Constitution = [10]
        self.Dexterity = [10]
        self.Intelligence = [10]
        self.Experience = 0
        self.Level = 0

    def IncreaseAtt(self,GameAttributes,amount):
        self.Strength[GameAttributes]+= amount
        self.Constitution[GameAttributes]+= amount
        self.Dexterity[GameAttributes]+= amount
        self.Intelligence[GameAttributes]+= amount

    def IncreaseExperience(self):
        return self.Experience

    def IncreaseLevel(self):
        if (self.Experience >= 1):
            self.Level += 1
            return self.Level