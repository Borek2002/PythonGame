from .plant import Plant

class Guarana (Plant):

    def __init__(self,world,point):
        super().__init__(world, point, 0, 0, 1, 1, True)

    def getColor(self):
        return "#FF1A00"

    def getName(self):
        return "Guarana"

    def clone(self,p):
        return Guarana(self.world,p)