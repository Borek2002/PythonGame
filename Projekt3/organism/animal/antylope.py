import random

from .animal import Animal

class Antylope (Animal):

    def __init__(self,world,point):
        super().__init__(world, point, 4, 4, 2, 1, True)

    def getColor(self):
        return "#FFB148"

    def getName(self):
        return "Antylope"

    def clone(self,p):
        return Antylope(self.world,p)

    def collision(self,oc):
        chance=random.randint(0,1)
        if chance==0 and isinstance(oc,Animal):
            while(True):
                p=self.newPosition()
                if self.world.getBoard()[p.getY()][p.getX()]==None:
                    self.world.comment.addComment(self.getName()+" run away from "+oc.getName())
                    self.makeMove(p)
                    break
                elif self.world.getBoard()[p.getY()][p.getX()].getStrenght()<=self.getStrenght():
                    super().collision(self.world.getBoard()[self.point.getY()][self.point.getX()])
                    break
        else:
            super().collision(oc)