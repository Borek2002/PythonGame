from .animal import Animal

class Sheep (Animal):

    def __init__(self,world,point,strenght=4,age=1):
        super().__init__(world, point, 4, strenght, 1, age, True)

    def getColor(self):
        return "#FFFFFF"

    def getName(self):
        return "Sheep"

    def clone(self,p):
        return Sheep(self.world,p)
