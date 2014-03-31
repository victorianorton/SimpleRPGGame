__author__ = 'Victoria'

from src.game.Heroes2 import *
#from src.game.Monsters2 import *


hero = Hero('hero')
room = Room1()
monst = Monster('monster')

#state = hero.runState.run()
#state = hero.roamState.attack()
# state = hero.attackState.attack()
#state = monst.
#roam = hero.currentState.north()

hero.addObserver(monst)
monst.addObserver(hero)
hero.roam()
room.accept(hero)
#monst.display()
#  hero.attack()
#monst.attack()
monst.roam()
#hero.attack(monst)
#room.accept(hero)

#room.attack(monst)