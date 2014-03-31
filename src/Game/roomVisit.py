__author__ = 'Victoria'

class Room(object):
    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def linkTo(self, room):
        self.link = room

    def printAll(self):
        print (self.value)
        if self.link is not None:
            self.link.printAll()

    def sum_v1(self, room, v):
        if room.link == None:
            return room.value + v
        else:
            return self.sum_v1(room.link, v + room.value)

    def sum_v2(self, v):
        if self.link == None:
            return self.value + v
        else:
            return self.link.sum_v2(v + self.value)

    def sum_v3(self):
        if self.link is None:
            return self.value
        else:
            return self.value + self.link.sum_v3()


    def sum_v4(self):
        if self.link:
            return self.value + self.link.sum_v4()
        else:
            return self.value


    def acceptVisitor(self, v):
        v.visit(self)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Castle(object):
    def __init__(self):
        self._room = None
        self._current = None
        print ('created a Castle with rooms')

    def __iter__(self):
        self._current = self._room
        return self

    def next(self):
        if self._current == None:
            raise StopIteration
        else:
            value = self._current.value
            self._current = self._current.link
            return value

    def append(self, item):
        self._room = Room(item, self._room)



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Visitor(object):
    def visit(self, room):
        pass

class SumVisitor(Visitor):
    def __init__(self):
        self.sum = 0

    def visit(self, room):
        self.sum += room.value
        if room.link is not None:
            room.link.acceptVisitor(self)

    def getSum(self):
        return self.sum


def printValues(room):
    while room is not None:
        print (room.value)
        room = room.link

def sum_iterative(room):
    v = 0
    while room:
        v += room.value
        room = room.link
    return v

def sum_recursive_v0(room, v):
    if room.link == None:
        return room.value + v
    else:
        return sum_recursive_v0(room.link, v + room.value)

def sum_recursive_v1(room):
    if room.link == None:
        return room.value
    else:
        return room.value + sum_recursive_v1(room.link)

c1 = Room(1)
c2 = Room(2)
c3 = Room(3)
c4 = Room(4)

c1.linkTo(c2)
c2.linkTo(c3)
c3.linkTo(c4)

print ("calling printCellValues(c1)")
printValues(c1)

print ("calling c1.printAll()")
c1.printAll()

print ("calling sum_iterative(c1)")
print (sum_iterative(c1))

print ("calling sum_recursive_v0(c1, 0)")
print (sum_recursive_v0(c1, 0))

print ("calling c1.sum_v1(c1, 0)")
print (c1.sum_v1(c1, 0))

print ("calling c1.sum_v2(0)")
print (c1.sum_v2(0))

print ("calling c1.sum_v3()")
print (c1.sum_v3())


print ("calling c1.sum_v4()")
print (c1.sum_v4())


print ("find the sum by using a SumVisitor")
sumVisitor = SumVisitor()
c1.acceptVisitor(sumVisitor)
print (sumVisitor.sum)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

castle = Castle()

castle.append(10)

for item in castle:
    print (item)

print ("now putting cells into the collection")
castle.append(c1)
castle.append(c2)
castle.append(c3)
castle.append(c4)


for item in castle:
    print (item.value)
