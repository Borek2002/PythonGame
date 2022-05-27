import random

from .plant import Plant

class Grass (Plant):

    def __init__(self,world,point):
        super().__init__(world, point, 0, 0, 1, 1, True)

    def getColor(self):
        return "#39DF00"

    def getName(self):
        return "Grass"

    def clone(self,p):
        return Grass(self.world,p)