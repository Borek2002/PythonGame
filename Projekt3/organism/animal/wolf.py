
from .animal import Animal


class Wolf(Animal):

    def __init__(self,world,point,strenght=9,age=1):
        super(Wolf,self).__init__(world,point,5,strenght,1,age,True)

    def getColor(self):
        return "#373737"

    def getName(self):
        return "Wolf"

    def clone(self,p):
        return Wolf(self.world,p)