__author__ = 'Victoria'

class AttackWeapon(object):
    def weapon(self):
        pass

class Weapons(AttackWeapon):
    def weapon(self):
        pass

#Specific Weapons
class Sword(AttackWeapon):
    def __init__(self):
        super(AttackWeapon, self).__init__()
    def weapon(self):
        print ("I am hurting you with my Sword!")

class Ax(AttackWeapon):
    def __init__(self):
        super(AttackWeapon, self).__init__()
    def weapon(self):
        print ("I am hurting you with my Ax!")

class BowArrow(AttackWeapon):
    def __init__(self):
        super(AttackWeapon, self).__init__()
    def weapon(self):
        print ("I am hurting you with my Bow and Arrow!")