__author__ = 'Victoria'

import Tkinter as tk
import threading

class GameCanvas(threading.Thread):
    def __init__(self , width = 400 , height = 400, gameworld = None, **kwargs ):
        super(GameCanvas,self).__init__(**kwargs)
        self._root = tk.Tk()
        self._canvas = tk.Canvas(self._root, width= width, height=height, bg = "black")
        self._canvas.pack()
        self._world = gameworld
        self._root.bind( "<Key>", self.keyHandler)

    def getCanvas(self):
        return self._canvas

    def redraw(self, listOfDrawables):
        self._canvas.delete(tk.ALL)
        for i in listOfDrawables:
            self._canvas.create_image(i.positionX, i.positionY, image = i.getSprite(), anchor = tk.CENTER)
        self._root.update()

    def keyHandler(self, Event):
        if (Event.keysym == "Up" or Event.keysym == "Down" or Event.keysym == "Left" or Event.keysym == "Right" ):
            self._world.playerMove(Event.keysym)