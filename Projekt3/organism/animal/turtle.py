import random

from .animal import Animal

class Turtle (Animal):

    def __init__(self,world,point):
        super().__init__(world, point, 1, 2, 1, 1, True)

    def getColor(self):
        return "#005800"

    def getName(self):
        return "Turtle"

    def clone(self,p):
        return Turtle(self.world,p)

    def action(self):
        chance=random.randint(0,2)
        if chance==1:
            super(Turtle,self).action()
        else:
            self.age+=1