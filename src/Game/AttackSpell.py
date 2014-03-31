__author__ = 'Victoria'

class AttackSpell(object):
    def spell(self):
        self.attackSpell = AttackSpell()

class Spells(AttackSpell):
    def spell(self):
        self.spell = []

#Specific Spells
class FireBall( AttackSpell):
    def __init__(self):
        super(AttackSpell, self).__init__()
    def spell(self):
        self.fireball = FireBall
        print ("I am attacking you with a Fireball")

class ThunderBolt(AttackSpell):
    def __init__(self):
        super(AttackSpell, self).__init__()
    def spell(self):
        print ("I am attacking you with a Thunderbolt")
        self.thunderbolt = ThunderBolt

class SpiritShield(AttackSpell):
    def __init__(self):
        super(AttackSpell, self).__init__()
    def spell(self):
        print ("I am attacking you with a Spirit Shield")
        self.spiritshield = SpiritShield
