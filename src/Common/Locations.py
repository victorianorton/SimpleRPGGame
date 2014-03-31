__author__ = 'Victoria'

import math

# Useful heading constants
DOWN=math.pi/float(2)
UP=(3*math.pi)/float(2)
LEFT=float(math.pi)
RIGHT=0.0

def distance(loc1,loc2):
    '''Computes the distance between two Locations'''
    return math.sqrt((loc1.x-loc2.x)**2+(loc1.y-loc2.y)**2)

class Location:
    '''Represents some location in the game world

    Screen Coordinates invert the Y axis so that up matches with cultural sensibilities (ie y=10 is visually higher than y=3).
    '''
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def getScreenCoordinates(self):
        '''Returns the location in screen coordinates'''
        return (int(self._x),int(-self._y))

    def setXY(self,x,y):
        self._x=x
        self._y=y

    def translateXY(self,dx,dy):
        '''Updates the location to world coordinates x+dx, y+dy'''
        self._x=self._x+dx
        self._y=self._y+dy

    def translateHM(self,heading,magnitude):
        '''Updates the location based on a heading and magnitude

        heading is in counter clockwise radians from the vector (1,0)
        '''
        dx=magnitude*math.cos(heading)
        dy=magnitude*math.sin(heading)
        self.translateXY(dx,dy)

    def clone(self):
        return Location(self.x, self.y)

    def __str__(self):
        return "("+str(self._x)+","+str(self._y)+")"

    # Properties are a pretty cool language feature...
    # Once you get used to them, you'll miss them in other languages
    def _getX(self):
        return self._x
    def _setX(self,v):
        self._x=v
    x=property(_getX,_setX,None,'x in world coordinates')

    def _getY(self):
        return self._y
    def _setY(self,v):
        self._y=v
    y=property(_getY,_setY,None,'y in world coordinates')


# Location unit test
if __name__=="__main__":
    l=Location(0,0)
    print ("(0,0) =?",l)
    l.translateHM(0,1)
    print ("(1,0) =?",l)
    l.translateHM(math.pi,2)
    print ("(-1,0) =?",l)
    l.translateHM(math.pi/2,1)
    print ("(-1,1) =?",l)
    o=Location(2,5)
    print ("5 =?",distance(l,o))