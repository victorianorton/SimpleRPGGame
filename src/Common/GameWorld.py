__author__ = 'Victoria'

from src.common.Locations import distance
from src.common.Observable import *

def collides(collidable1, collidable2):
    '''detects if two collidables have collided'''
    if not isinstance(collidable1, GameCollidable):
        raise TypeError("Attempting to collide a non-collidable, argument 1")
    if not isinstance(collidable2, GameCollidable):
        raise TypeError("Attempting to collide a non-collidable, argument 2")
    r = collidable1.collisionRadius + collidable2.collisionRadius
    return r > distance(collidable1.location, collidable2.location)

#
# Multiple inheritance rules are pretty messy... however since some drawable things may not be collidable,
# using multiple inheritance may be appropriate. To make that work, everything in the inheritance chain should
# have similar initializers. If these initializers look a little like magic, they are.
#

class GameLocatable(object):
    '''Super class for everything that we might need to know the location of'''

    def __init__(self, initialLocation = None, **kwds):
        super(GameLocatable,self).__init__()
        if initialLocation is None:
            raise AttributeError("GameLocatables must recieve an initialLocation")
        self._location = initialLocation

    def getLocation(self):
        return self._location

    def updateLocation(self,newLocation):
        self._location.setXY(newLocation.x, newLocation.y)

    location = property(getLocation, updateLocation, None, 'Location of the drawable')

class GameDrawable(GameLocatable):
    '''Super class for everything that we might draw'''
    def __init__(self, **kwds):
        super(GameDrawable,self).__init__(**kwds)
        self._picture =  None

    def setSprite(self,image):
        self._picture = image

    def getSprite(self):
        return self._picture


class GameCollidable(GameLocatable):
    '''Super class for everything that we should resolve collisions for'''

    def __init__(self, collisionRadius = None, **kwds):
        if collisionRadius is None:
            raise AttributeError("GameCollidables must receive a collisionRadius")
        super(GameCollidable, self).__init__(**kwds)
        self._radius = collisionRadius

    def setCollisionRadius(self, newCollisionRadius):
        self._radius = newCollisionRadius

    def getCollisionRadius(self):
        return self._radius

    collisionRadius = property(getCollisionRadius, setCollisionRadius, None, 'Location of the drawable')


class GameWorld(Observer):
    '''Represents some game world we can visualize'''

    def __init__(self, **kwds):
        super(GameWorld, self).__init__(**kwds)
        self._moveableList = list()
        self._immovableList = list()
        self._collidable = list()
        self._drawable = list()
        self._gameCanvas = None

    def setPlayer(self, unit):
        '''Sets the unit controlled by the player'''
        assert unit in self._moveableList
        self._avatar=unit

    def playerMove(self, direction):
        '''Forwards a move to the player's avatar'''
        self._avatar.move(direction)

    def setGameCanvas(self, gameCanvas):
        assert self._gameCanvas is None
        self._gameCanvas = gameCanvas

    def getGameCanvas(self):
        return self._gameCanvas

    gameCanvas = property(getGameCanvas, setGameCanvas, None, 'Canvas where the game is drawn')

    def move(self, obj, heading, distance):
        '''Attempts to move the object. If there is a collision the location is reset to the old location
         and an exception is raised
        '''
        assert obj in self._moveableList
        oldLocation = obj._location.clone()
        obj._location.translateHM(heading, distance)
        if isinstance(obj,GameCollidable):
            for other in self._collidable:
                if obj is other:
                    continue
                if collides(obj, other):
                    obj._location=oldLocation
                    raise CollisionOccurred(str(obj) + " collided with " + str(other), obj, other)

        self.reDraw()
    def addStationaryWorldObject(self, newObject):
        assert isinstance(newObject, GameLocatable)
        self._immovableList.append(newObject)

        if isinstance(newObject, GameDrawable):
            self._drawable.append(newObject)

        if isinstance(newObject, GameCollidable):
            self._collidable.append(newObject)

    def addWorldObject(self, newObject):
        assert isinstance(newObject, GameLocatable)
        self._moveableList.append(newObject)
        newObject.addObserver(self)
        if isinstance(newObject, GameDrawable):
            self._registerDrawable(newObject)

        if isinstance(newObject, GameCollidable):
            self._collidable.append(newObject)

    def removeWorldObject(self, oldObject):
        if oldObject in self._moveableList:
            self._moveableList.remove(oldObject)
            oldObject.removeObserver(self)
        if oldObject in self._immovableList:
            self._immovableList.remove(oldObject)
        if oldObject in self._collidable:
            self._collidable.remove(oldObject)
        if oldObject in self._drawable:
            self._unregisterDrawable(oldObject)
        self.reDraw()

    def _registerDrawable(self, obj):
        assert isinstance(obj, GameDrawable)
        self._drawable.append(obj)
        self.reDraw()

    def _unregisterDrawable(self, obj):
        assert isinstance(obj, GameDrawable)
        assert obj in self._drawable
        self._drawable.remove(obj)

    def reDraw(self):
        self._gameCanvas.redraw(self._drawable)

    def update(self, observable):
        self.move(observable, observable._lastDirection, observable._stepDistance)

class CollisionOccurred(Exception):
    def __init__(self, msg=None, obj1=None, obj2=None, **kwargs):
        assert msg is not None
        assert obj1 is not None
        assert obj2 is not None
        super(CollisionOccurred, self).__init__(msg, **kwargs)
        self.object1 = obj1
        self.object2 = obj2

    def __str__(self):
        return self.msg