
from .animal import Animal


class Wolf(Animal):

    def __init__(self,world,point,age):
        super(Wolf,self).__init__(world,point,5,9,1,age,True)

    def getColor(self):
        return "#000000"