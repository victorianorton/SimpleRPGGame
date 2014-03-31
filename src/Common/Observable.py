__author__ = 'Victoria'

class Observable(object):
    def __init__(self, **kwds):
        super(Observable, self).__init__(**kwds)
        self._observers = []
    def addObserver(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)
    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self)


class Observer(object):
    def __init__(self, **kwds):
        super(Observer, self).__init__(**kwds)
    def update(self, observable):
        pass
