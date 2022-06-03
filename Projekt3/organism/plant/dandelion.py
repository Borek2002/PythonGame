import random

from .plant import Plant

class Dandelion (Plant):

    def __init__(self,world,point,strenght=0,age=1):
        super().__init__(world, point, 0, strenght, 3, age, True)

    def getColor(self):
        return "#FDFF20"

    def getName(self):
        return "Dandelion"

    def clone(self,p):
        return Dandelion(self.world,p)