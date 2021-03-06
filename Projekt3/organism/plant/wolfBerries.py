from .plant import Plant

class WolfBerries (Plant):

    def __init__(self,world,point,strenght=99,age=1):
        super().__init__(world, point, 0, strenght, 1, age, True)

    def getColor(self):
        return "#C000E7"

    def getName(self):
        return "Berries"

    def clone(self,p):
        return WolfBerries(self.world,p)