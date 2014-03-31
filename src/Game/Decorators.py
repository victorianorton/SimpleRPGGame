__author__ = 'Victoria'

#Decorator Pattern in Characters
class BarDecorators(Barbarian):
    pass
class ImageBarDecorator(BarDecorators):
    def __init__(self, decorated, picFile):
        self.decorated = decorated
        self.picFile = picFile
        super(ImageBarDecorator, self).__init__(self.decorated.canvas,
                                                self.decorated.positionX, self.decorated.positionY, self.decorated.name, self.decorated.picFile)
class FastBarMoveDecorator(BarDecorators):
    def __init__(self, decorated):
        self.decorated = decorated()
        super(FastBarMoveDecorator, self).__init__(self.decorated.canvas,
                                                   self.decorated.positionX, self.decorated.positionY, self.decorated.name, self.decorated.picFile)

#Decorator Pattern in Monsters
class DragDecorators(Dragon):
    pass
class ImageDragDecorator(DragDecorators):
    def __init__(self, decorated, picFile):
        self.decorated = decorated
        self.picFile = picFile
        super(ImageDragDecorator, self).__init__(self.decorated.canvas,
                                                 self.decorated.positionX, self.decorated.positionY, self.decorated.name, self.decorated.picFile)
class FastDragMoveDecorator(DragDecorators):
    def __init__(self, decorated):
        self.decorated = decorated
        super(FastDragMoveDecorator, self).__init__(self.decorated.canvas,
                                                    self.decorated.positionX, self.decorated.positionY, self.decorated.name, self.decorated.picFile)
