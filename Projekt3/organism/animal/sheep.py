from .animal import Animal

class Sheep (Animal):

    def __init__(self,world,point):
        super().__init__(world, point, 4, 4, 1, 1, True)

    def getColor(self):
        return "#FFFFFF"

    def getName(self):
        return "Sheep"

    def clone(self,p):
        return Sheep(self.world,p)
