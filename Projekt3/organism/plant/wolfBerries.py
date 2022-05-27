from .plant import Plant

class WolfBerries (Plant):

    def __init__(self,world,point):
        super().__init__(world, point, 0, 99, 1, 1, True)

    def getColor(self):
        return "#C000E7"

    def getName(self):
        return "Berries"

    def clone(self,p):
        return WolfBerries(self.world,p)