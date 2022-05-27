import random

from .plant import Plant

class Dandelion (Plant):

    def __init__(self,world,point):
        super().__init__(world, point, 0, 0, 3, 1, True)

    def getColor(self):
        return "#FDFF20"

    def getName(self):
        return "Dandelion"

    def clone(self,p):
        return Dandelion(self.world,p)