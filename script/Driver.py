__author__ = 'Victoria'

#from src.game.Creature import *
from src.game.Heroes import *
from src.game.Monsters import *

hero = Hero('hero')
monst = Monster('monst')

monst.addObserver(monst)
monst.addObserver(monst)

hero.Display()
monst.Display()

Commands = {
    'north' : Creatures.north,
    'south' : Creatures.south,
    'east' : Creatures.east,
    'west' : Creatures.west,
    'room' : Hero.castleRoom,
    'level': Hero.levelStatus,
    'experience' : Hero.experStatus,
    'health': Hero.healthStatus,
    'attack' : Hero.attack,
    'run' : Hero.run,
    'rest': Hero.rest,
    'quit': Hero.quit,
    }

print ("Here is a list of commands you can use : \n%s\n" % Commands.keys())
print ("You are a Hero that is searching for an adventure...\n")
print ("What direction would you like to move in?")


while(hero._health > 0):
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](hero)
                commandFound = True
               # print Commands.keys()
                break
        if not commandFound:
            print ("Hero does not understand that command")

for room in CastleRoomGen(1):
    hero.planMove()
    hero.act()
    room.accept(hero)
    if room.occupy:
        monst.planMove()
        monst.act()
        room.accept(monst)