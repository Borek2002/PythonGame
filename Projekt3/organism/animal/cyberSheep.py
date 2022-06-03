from .animal import Animal
from ...point import Point


class CyberSheep (Animal):

    def __init__(self,world,point,strenght=11,age=1):
        super().__init__(world, point, 4, strenght, 1, age, True)

    def getColor(self):
        return "#70FFFF"

    def getName(self):
        return "CyberSheep"

    def clone(self,p):
        return CyberSheep(self.world,p)

    def action(self):
        nearestBorscht=None
        distance=100000
        move=Point(0,0)
        for i in range(len(self.world.organismList)):
            if self.world.organismList[i].getName()=="Borscht":

                if (self.checkDistance(self.world.organismList[i])<distance):
                    distance=self.checkDistance(self.world.organismList[i])
                    nearestBorscht=self.world.organismList[i]
        if nearestBorscht!=None:
            if self.point.getX()-nearestBorscht.point.getX()<0:
                move.setX(1)
            elif self.point.getX()-nearestBorscht.point.getX()>0:
                move.setX(-1)
            elif self.point.getY()-nearestBorscht.point.getY()<0:
                move.setY(1)
            elif self.point.getY()-nearestBorscht.point.getY()>0:
                move.setY(-1)
            newPoint=Point(self.point.getX()+move.getX(),self.point.getY()+move.getY())
            if self.world.board[newPoint.getY()][newPoint.getX()]==None:
                self.world.comment.addComment(
                    self.getName() + " move from (x: " + str(self.point.getX()) + ", y: " + str(
                        self.point.getY()) + ") to (x: " + str(newPoint.getX()) + ", y: " + str(newPoint.getY()) + ")")
                self.makeMove(newPoint)
            else:
                super(CyberSheep, self).collision(self.world.board[newPoint.getY()][newPoint.getX()])
        else:
            super(CyberSheep, self).action()


    def checkDistance(self,other):
        return (self.point.getX()-other.point.getX())**2+(self.point.getY()-other.point.getY())**2