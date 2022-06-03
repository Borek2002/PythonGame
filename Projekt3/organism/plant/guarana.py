from .plant import Plant

class Guarana (Plant):

    def __init__(self,world,point,strenght=0,age=1):
        super().__init__(world, point, 0, strenght, 1, age, True)

    def getColor(self):
        return "#FF1A00"

    def getName(self):
        return "Guarana"

    def clone(self,p):
        return Guarana(self.world,p)