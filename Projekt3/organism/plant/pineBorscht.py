
from .plant import Plant
from ..animal import Animal


class PineBorscht (Plant):

    def __init__(self,world,point,strenght=10,age=1):
        super().__init__(world, point, 0,strenght, 1, age, True)

    def getColor(self):
        return "#0019CF"

    def getName(self):
        return "Borscht"

    def clone(self,p):
        return PineBorscht(self.world,p)

    def action(self):
        if self.point.getY()>0:
            if isinstance(self.world.getBoard()[self.point.getY()-1][self.point.getX()],Animal) and self.world.getBoard()[self.point.getY()-1][self.point.getX()].getName()!="CyberSheep":
                self.world.comment.addComment("Pine Borscht kill "+self.world.getBoard()[self.point.getY()-1][self.point.getX()].getName())
                self.world.removeOrganism(self.world.getBoard()[self.point.getY()-1][self.point.getX()])
        if self.point.getY()<self.world.worldHeight-1:
            if isinstance(self.world.getBoard()[self.point.getY()+1][self.point.getX()],Animal) and self.world.getBoard()[self.point.getY()+1][self.point.getX()].getName()!="CyberSheep":
                self.world.comment.addComment("Pine Borscht kill "+self.world.getBoard()[self.point.getY()+1][self.point.getX()].getName())
                self.world.removeOrganism(self.world.getBoard()[self.point.getY()+1][self.point.getX()])

        if self.point.getX()>0:
            if isinstance(self.world.getBoard()[self.point.getY()][self.point.getX()-1],Animal) and self.world.getBoard()[self.point.getY()][self.point.getX()-1].getName()!="CyberSheep":
                self.world.comment.addComment("Pine Borscht kill "+self.world.getBoard()[self.point.getY()][self.point.getX()-1].getName())
                self.world.removeOrganism(self.world.getBoard()[self.point.getY()][self.point.getX()-1])

        if self.point.getX()<self.world.worldWidth-1:
            if isinstance(self.world.getBoard()[self.point.getY()][self.point.getX()+1],Animal) and self.world.getBoard()[self.point.getY()][self.point.getX()+1].getName()!="CyberSheep":
                self.world.comment.addComment("Pine Borscht kill "+self.world.getBoard()[self.point.getY()][self.point.getX()+1].getName())
                self.world.removeOrganism(self.world.getBoard()[self.point.getY()][self.point.getX()+1])

        super().action()