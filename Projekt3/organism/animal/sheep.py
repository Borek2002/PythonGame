from .animal import Animal

class Sheep (Animal):

    def __init__(self,world,point,age):
        super().__init__(world, point, 5, 9, 1, age, True)

    def getColor(self):
        return "#FFFFFF"