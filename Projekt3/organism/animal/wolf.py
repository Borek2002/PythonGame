
from .animal import Animal


class Wolf(Animal):

    def __init__(self,world,point):
        super(Wolf,self).__init__(world,point,5,9,1,1,True)

    def getColor(self):
        return "#373737"

    def getName(self):
        return "Wolf"

    def clone(self,p):
        return Wolf(self.world,p)